import os
import subprocess
import sys
import cv2
from picamera2 import Picamera2
import numpy as np

from src.ui_DETECTOR_7inch import Ui_MainWindow
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
)
from PySide6.QtCore import QTimer, Signal, Slot
from PySide6.QtGui import QImage, QPixmap, QMovie
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from datetime import datetime
from time import sleep

from resources.ConfigManager import ConfigManager
from resources.Rectangle import Rectangle
from resources.Keyboard import Keyboard
from resources.Camera import CameraView, RectangleSettings
from resources.Datetime import ShowDateTime
from resources.Alert import Alert, BUZZER
from gpiozero import LED

# from resources.Animation import AnimatedWidgetHelper

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
SAVE_IMAGES_DIR = os.path.join(BASE_DIR, "captured_images")  # โฟล์เดอร์สำหรับบันทึกภาพ
os.makedirs(SAVE_IMAGES_DIR, exist_ok=True)
GIF_FILE = os.path.join(BASE_DIR, "gui", "assets", "gif", "connecting.gif")

def cvimg_to_qpixmap(cv_img: np.ndarray) -> QPixmap:
    """แปลงภาพ OpenCV -> QPixmap"""
    if cv_img.ndim == 2:
        h, w = cv_img.shape
        qimg = QImage(cv_img.data, w, h, w, QImage.Format.Format_Grayscale8)
    else:
        h, w, ch = cv_img.shape
        rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        qimg = QImage(rgb.data, w, h, ch * w, QImage.Format.Format_RGB888)
    return QPixmap.fromImage(qimg)

class LMEDetect(QMainWindow, Ui_MainWindow):
    def __init__(self, os_name="Windows"):
        """
        """
        super().__init__()
        self.setupUi(self)
        self.os_name = os_name

        process_gif = QMovie(GIF_FILE)
        self.process_img.setMovie(process_gif)
        process_gif.start()

        self.showDateTime = ShowDateTime(self.date_bar, self.time_bar)
        self.showDateTime.show()

        self.show_sidebar.setHidden(True)
        self.currentPage = self.process_page
        self.stackedWidget.setCurrentWidget(self.currentPage)
        self._addEventListener()

        self.config = ConfigManager()

        # โหลด counter
        counter = self.config.get_count()
        self.countOK = counter.ok
        self.countNG = counter.ng
        self.countTotal = counter.ok + counter.ng
        self.count_ok.setText(f"{self.countOK:,}")
        self.count_ng.setText(f"{self.countNG:,}")
        self.count_total.setText(f"{(self.countTotal):,}")
        self.buzzer = LED(19)

        # โหลด rectangle
        _rectangle = self.config.get_rectangle()
        self.rectangle = Rectangle(self.webcam_setting_monitor)
        self.rectangle.set_rectangle_from_image_coords(_rectangle)
        self.rectangle.show()  # ต้องเรียก show() เพื่อแสดงวิดเจ็ต
        self.webcam_setting_monitor.installEventFilter(self.rectangle)
        self.rectangle.rect_drawn.connect(self.setRectangle)

        picam2 = Picamera2()
        self.cameraView = CameraView(monitor=self.webcam_monitor, camera=picam2, rectangle=_rectangle, sensorPin=22, flashLightPin=24)
        self.cameraView.start()

        self.cameraView.updateDetectImage.connect(self._isDetect)
        self.detectionAlert = Alert(self.detection_alert)

        # self.camera_setting_1.setHidden(True)
        # self.camera_setting_2.setHidden(True)

    # เพิ่ม Event
    def _addEventListener(self):
        self.home_1.clicked.connect(lambda: self._switchToPage(self.detection_page, self.webcam_monitor))
        self.home_2.clicked.connect(lambda: self._switchToPage(self.detection_page, self.webcam_monitor))
        self.setting_1.clicked.connect(lambda: self._switchToPage(self.lme_settings_page, self.webcam_setting_monitor))
        self.setting_2.clicked.connect(lambda: self._switchToPage(self.lme_settings_page, self.webcam_setting_monitor))
        self.camera_setting_1.clicked.connect(lambda: self._switchToPage(self.camera_setting_page, self.camera_setting_monitor))
        self.camera_setting_2.clicked.connect(lambda: self._switchToPage(self.camera_setting_page, self.camera_setting_monitor))

        self.capture_set.clicked.connect(self.capTemplateLme)
        self.save_set.clicked.connect(self.setTemplateLme)

        self.shutdown_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.shutdown_page))
        self.shutdown_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.shutdown_page))

        self.start.clicked.connect(self.startDetection)
        self.capture_test.clicked.connect(lambda: self._isDetect(True))
        self.restart_program_1.clicked.connect(self.restart)
        self.restart_program_2.clicked.connect(self.restart)
        self.cancel_shutdown.clicked.connect(lambda: self.shutdownHandler(False))
        self.confirm_shutdown.clicked.connect(lambda: self.shutdownHandler(True))
        self.count_reset.clicked.connect(self._countReset)

    # เปลี่ยนหน้าต่างแสดงผล
    def _switchToPage(self, page: QWidget, monitor: QLabel = None):
        self.stackedWidget.setCurrentWidget(page)
        self.currentPage = page
        page_name = page.objectName()
        if monitor:
            self.cameraView.monitor = monitor

        if page_name == "detection_page":
            self.cameraView.isShowRect = True
        elif page_name == "lme_settings_page":
            template = self.config.get_template()
            _lot = template.lot
            _mfg = template.mfg
            _exp = template.exp

            self.lot_set.setText(_lot)
            self.mfg_set.setText(_mfg)
            self.exp_set.setText(_exp)
            self.cameraView.isShowRect = False
        else:
            self.cameraView.isShowRect = False

    @Slot(int, int, int, int)  # ตั้งค่า rectangle x1, y1, x2, y2
    def setRectangle(self, x1, y1, x2, y2):
        # สร้างออบเจ็กต์ RectangleSettings
        rect = RectangleSettings(X1=x1, Y1=y1, X2=x2, Y2=y2)

        # คำนวณขนาด
        width = abs(rect.X2 - rect.X1)
        height = abs(rect.Y2 - rect.Y1)

        print(f"ตำแหน่งกรอบ: x1={x1}, y1={y1}, x2={x2}, y2={y2}")
        print(f"ความกว้าง: {width} พิกเซล, ความสูง: {height} พิกเซล")

        if width > 150 and height > 50:
            self.cameraView.rectangle = rect
            self.config.update_rectangle(rect)
        else:
            _X1 = self.cameraView.rectangle.X1
            _Y1 = self.cameraView.rectangle.Y1
            _X2 = self.cameraView.rectangle.X2
            _Y2 = self.cameraView.rectangle.Y2
            rect = RectangleSettings(X1=_X1, Y1=_Y1, X2=_X2, Y2=_Y2)
            self.rectangle.set_rectangle_from_image_coords(rect)

    # อ่าน lot, mfg, exp จากฉลาก
    def capTemplateLme(self):
        timestamp, processing_time, lme, image, process_img = self.cameraView.captured(isDetect=True)
        frame = np.ascontiguousarray(image)  # This ensures C-contiguous memory layout

        height, width, channel = frame.shape
        bytes_per_line = channel * width

        # Add processing time text to the image
        text = f"{timestamp:s} {processing_time:.2f}ms"
        font = cv2.FONT_HERSHEY_TRIPLEX
        font_scale = (width / 250) * 0.4
        font_color = (0, 0, 255)  # BGR
        thickness = 1
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = int((width - text_size[0]) / 2)  # center
        text_y = height - 5  # 5 pixels from the bottom
        cv2.putText(
            frame,
            text,
            (text_x, text_y),
            font,
            font_scale,
            font_color,
            thickness,
        )

        q_image = QImage(
            frame.data,
            width,
            height,
            bytes_per_line,
            QImage.Format.Format_BGR888,
        )
        self.webcam_setting_view.setPixmap(QPixmap.fromImage(q_image))

        try:
            lmf_label: list[QLabel] = [self.lot_set, self.mfg_set, self.exp_set]
            for i, w in enumerate(lme if lme else ['', '', '']):
                lmf_label[i].setText(w if w else "XXXXXX")
        except Exception as err:
            pass

    # บันทึกการตั้งค่า lot, mfg, exp และ rectangle
    def setTemplateLme(self):
        lot = self.lot_set.text()
        lot = None if lot == "XXXXXX" else lot

        mfg = self.mfg_set.text()
        mfg = None if mfg == "XXXXXX" else mfg

        exp = self.exp_set.text()
        exp = None if exp == "XXXXXX" else exp

        if lot and mfg and exp:
            self.config.update_template(lot, mfg, exp)

    # เริ่มการตรวจจับ
    def startDetection(self):
        isRunning = self.start.isChecked()
        self.cameraView.liveView(not isRunning)
        self.setting_1.setHidden(isRunning)
        self.setting_2.setHidden(isRunning)
        self.camera_setting_1.setHidden(isRunning)
        self.camera_setting_2.setHidden(isRunning)
        self.capture_test.setHidden(isRunning)

        if isRunning:
            self.start.setText("STOP")
            self.detection_status.setText("เริ่มการตรวจจับ")
        else:
            self.start.setText("START")
            self.detection_status.setText("กดปุ่ม START เพื่อเริ่มทำงาน")

    @Slot()  # อัพเดท detect monitor
    def _isDetect(self, isTesting=False):
        timestamp, processing_time, lme, image, process_img = self.cameraView.captured(isDetect=True)
        frame = np.ascontiguousarray(image)  # This ensures C-contiguous memory layout
        height, width, channel = frame.shape
        bytes_per_line = channel * width

        # Add processing time text to the image
        text = f"{timestamp:s} {processing_time:.2f}ms"
        font = cv2.FONT_HERSHEY_TRIPLEX
        font_scale = (width / 250) * 0.4
        font_color = (0, 0, 255)  # BGR
        thickness = 1
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = (width - text_size[0]) // 2
        text_y = height - 5  # 5 pixels from the bottom
        cv2.putText(
            frame,
            text,
            (text_x, text_y),
            font,
            font_scale,
            font_color,
            thickness,
        )

        # q_image = QImage(
        #     frame.data,
        #     width,
        #     height,
        #     bytes_per_line,
        #     QImage.Format.Format_BGR888,
        # )
        # ------------------------
        # แสดงผล
        # ------------------------
        pix = cvimg_to_qpixmap(frame)
        self.detection_view.setPixmap(pix)
        try:
            statusCheck = True
            _temp = self.config.get_template()
            _lme = [_temp.lot, _temp.mfg, _temp.exp]
            lmf_label: list[QLabel] = [self.lot_detected, self.mfg_detected, self.exp_detected]
            for i, w in enumerate(lme if lme else ['', '', '']):
                lmf_label[i].setText(w if w else "XXXXXX")
                if _lme[i] != w:
                    statusCheck = False
                    # widget.setStyleSheet("color: rgb(255, 0, 0)")

            initial_style = self.detection_alert.styleSheet()

            if statusCheck:
                if not isTesting:
                    self.countOK += 1
                    self.config.update_counter(ok=1)

                self.count_ok.setText(f"{self.countOK:,}")
                self.detection_alert.setText("OK")
                self.detection_alert.setStyleSheet(f"{initial_style} background-color: rgb(0, 170, 127);")
                self.buzzer.blink(0.1, 0.1, 1, True)
                
            else:
                if not isTesting:
                    self.countNG += 1
                    self.config.update_counter(ng=1)
                    
                self.count_ng.setText(f"{self.countNG:,}")
                self.detection_alert.setText("NG")
                self.detection_alert.setStyleSheet(f"{initial_style} background-color: rgb(255, 17, 17);")
                self.buzzer.blink(0.1, 0.1, 5, True)

            self.count_total.setText(f"{self.countOK + self.countNG:,}")

        except Exception as err:
            pass

    # รีเซ็ต counter
    def _countReset(self):
        self.countOK = 0
        self.countNG = 0
        self.countTotal = 0
        self.count_ok.setText(str(self.countOK))
        self.count_ng.setText(str(self.countNG))
        self.count_total.setText(str(self.countTotal))
        self.config.reset_counters()

    # รีสตาร์ทโปรแกรม
    def restart(self):
        """รีสตาร์ทโปรแกรม"""
        QApplication.quit()
        python = sys.executable
        script = sys.argv[0]  # main.py
        # เปิดโปรแกรมใหม่เป็น process ใหม่
        subprocess.Popen([python, script])
        # ปิดโปรแกรมเก่า
        
    # จัดการการปิดเครื่อง
    def shutdownHandler(self, shutdown=True):
        if shutdown and self.os_name == "Linux":
            print("*** Shutting down")
            sleep(1)
            os.system("sudo poweroff")
        elif not shutdown:
            self._switchToPage(self.currentPage)

    # ปิดโปรแกรม
    def closeEvent(self, event):
        self.cameraView.close()
        self.showDateTime.stop()
        super().closeEvent(event)
