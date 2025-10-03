import os
import subprocess
import sys
import re
import cv2
from picamera2 import Picamera2
import queue
import numpy as np

from src.ui_DETECTOR_7inch import Ui_MainWindow
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
)
from PySide6.QtCore import QTimer, Signal, Slot, Qt
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
from resources.Ocr import OcrWorker
from resources.QPixmapUtil import QPixmapUtil
from resources.Rejection import RejectionWorker
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

        # อ่านข้อมูลการตั้งค่าจากไฟล์ yml
        self.config = ConfigManager()

        # =====  lot,mfg,exp template ===== 
        template = self.config.get_template()
        self.lot = template.lot
        self.mfg = template.mfg
        self.exp = template.exp

        # =====  counter ===== 
        counter = self.config.get_count()
        self.countOK = counter.ok
        self.countNG = counter.ng
        self.countTotal = counter.ok + counter.ng
        self.count_ok.setText(f"{self.countOK:,}")
        self.count_ng.setText(f"{self.countNG:,}")
        self.count_total.setText(f"{(self.countTotal):,}")
        self.buzzer = LED(19)

        # =====  rectangle ===== 
        _rectangle = self.config.get_rectangle()
        self.rectangle = Rectangle(self.webcam_setting_monitor)
        self.rectangle.set_rectangle_from_image_coords(_rectangle)
        self.rectangle.show()  # ต้องเรียก show() เพื่อแสดงวิดเจ็ต
        self.webcam_setting_monitor.installEventFilter(self.rectangle)
        self.rectangle.rect_drawn.connect(self.setRectangle)

        # ===== Camera =====
        self.cropped_frame = None

        picam2 = Picamera2()
        self.monitor = self.webcam_monitor # หน้าจอแสดง frame
        self.cameraView = CameraView(monitor=self.monitor, camera=picam2, rectangle=_rectangle, flashLightPin=24)
        self.cameraView.start()

        # ===== Queue OCR V1 =====
        self.task_queue = queue.Queue()
        self.ocr_worker = OcrWorker(self.task_queue)
        self.ocr_worker.finished.connect(self.detection_ocr_result)
        self.ocr_worker.start()

        # ===== Queue OCR V2 =====
        # self.ocr = OcrWorker()
        # self.ocr.finished.connect(self.detection_ocr_result)

        # ===== Sensor =====
        self.sensor = Button(pin=pins.DI0, pull_up=False, bounce_time=0.02)
        self.sensor.when_pressed = self._detection

        # ===== Rejection =====
        self.rejection = RejectionWorker(sensorPin=pins.DI1, inputPullUp=False, rejectPin=pins.LED0, startReject=3, rejectDelay=0.5)
        self.rejection.rejected_signal.connect(lambda tag: print(f"GUI: {tag} ถูก reject!"))
        self.rejection.start()

        # ===== Alert ===== 
        self.detectionAlert = Alert(self.detection_alert)
        # self.camera_setting_1.setHidden(True)
        # self.camera_setting_2.setHidden(True)

        # ===== สร้างและตั้งค่า Virtual Keyboard =====
        # self.setupVirtualKeyboard()

    # ===== เพิ่ม Event ===== 
    def _addEventListener(self):
        self.home_1.clicked.connect(lambda: self._switchToPage(self.detection_page, self.webcam_monitor))
        self.home_2.clicked.connect(lambda: self._switchToPage(self.detection_page, self.webcam_monitor))
        self.setting_1.clicked.connect(lambda: self._switchToPage(self.lme_settings_page, self.webcam_setting_monitor))
        self.setting_2.clicked.connect(lambda: self._switchToPage(self.lme_settings_page, self.webcam_setting_monitor))
        self.camera_setting_1.clicked.connect(lambda: self._switchToPage(self.camera_setting_page, self.camera_setting_monitor))
        self.camera_setting_2.clicked.connect(lambda: self._switchToPage(self.camera_setting_page, self.camera_setting_monitor))

        # ทดสอบการตรวจจับ
        self.capture_test.clicked.connect(self._test_detection)

        # self.capture_set.clicked.connect(self.capTemplateLme)
        self.save_set.clicked.connect(self.setTemplateLme)

        self.shutdown_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.shutdown_page))
        self.shutdown_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.shutdown_page))

        self.start.clicked.connect(self.startDetection)
        self.restart_program_1.clicked.connect(self.restart)
        self.restart_program_2.clicked.connect(self.restart)
        self.cancel_shutdown.clicked.connect(lambda: self.shutdownHandler(False))
        self.confirm_shutdown.clicked.connect(lambda: self.shutdownHandler(True))
        self.count_reset.clicked.connect(self._countReset)

    # ===== เปลี่ยนหน้าต่างแสดงผล ===== 
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

    # ===== บันทึกการตั้งค่า lot, mfg, exp และ rectangle ===== 
    def setTemplateLme(self):
        lot = self.lot_set.text()
        lot = None if lot == "XXXXXX" else lot

        mfg = self.mfg_set.text()
        mfg = None if mfg == "XXXXXX" else mfg

        exp = self.exp_set.text()
        exp = None if exp == "XXXXXX" else exp

        if lot and mfg and exp:
            self.config.update_template(lot, mfg, exp)

    # ===== เริ่มการตรวจจับ ===== 
    def startDetection(self):
        isRunning = self.start.isChecked()
        self.cameraView.liveView(not isRunning)
        # self.setting_1.setHidden(isRunning)
        # self.setting_2.setHidden(isRunning)
        # self.camera_setting_1.setHidden(isRunning)
        # self.camera_setting_2.setHidden(isRunning)
        # self.capture_test.setHidden(isRunning)

        if isRunning:
            self.start.setText("STOP")
            self.detection_status.setText("เริ่มการตรวจจับ")
        else:
            self.start.setText("START")
            self.detection_status.setText("กดปุ่ม START เพื่อเริ่มทำงาน")

    # ===== ทดสอบตรวจจับการพิมพ์ ===== 
    def _test_detection(self):
        X1 = self.cameraView.rectangle.X1
        Y1 = self.cameraView.rectangle.Y1
        X2 = self.cameraView.rectangle.X2
        Y2 = self.cameraView.rectangle.Y2

        frame = self.cameraView.captured()
        self.cropped_frame = frame[Y1:Y2, X1:X2]
        processed_image, preprocessed_image, text, processing_time = self.ocr_worker.detect_and_recognize_text(self.cropped_frame)
        print("(Camera detected a message)=> ")
        print(f"Processing in: {processing_time:.4f}s")
        q_img = QPixmapUtil.from_cvimg(processed_image)
        self.detection_view.setPixmap(q_img)

        lmf_label: list[QLabel] = [self.lot_detected, self.mfg_detected, self.exp_detected]
        statusCheck = self._parse_lme(text, lmf_label)
        self._update_ui_detection(statusCheck, isTesting=False)

    # ===== ตรวจจับการพิมพ์ ===== 
    def _detection(self, sensor):
        isRunning = self.start.isChecked()
        if sensor and isRunning:
            # self.buzzer.blink(0.1, 0.1, 1, True)
            X1 = self.cameraView.rectangle.X1
            Y1 = self.cameraView.rectangle.Y1
            X2 = self.cameraView.rectangle.X2
            Y2 = self.cameraView.rectangle.Y2
                
            frame = self.cameraView.captured()
            q_img = QPixmapUtil.from_cvimg(frame)
            self.monitor.setPixmap(q_img)

        self.cropped_frame = frame[Y1:Y2, X1:X2]
        self.task_queue.put(self.cropped_frame) # version 1 แบบ Queue + QThread
        # self.ocr.run_ocr(cropped_frame) # version 2 แบบ ThreadPoolExecutor

    # ===== ตรวจสอบ Lot / MFG / EXP =====
    def _parse_lme(self, text: str, lmf_label: list[QLabel]):
        statusCheck = True

        try:
            # หา Lot No. → ตัวเลข 5 หลัก
            lot_match = re.search(r"\s*\|?\s*(\d{5})", text)
            lot_no = lot_match.group(1) if lot_match else None

            # หา MFG / EXP → รูปแบบ dd/mm/yy
            dates = re.findall(r"\d{2}/\d{2}/\d{2}", text)
            mfg_date = dates[0] if len(dates) >= 1 else None
            exp_date = dates[1] if len(dates) >= 2 else None

            now = datetime.now()
            timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")
            print("Timestamp: ", timestamp)
            print("Results: ", text.split("\n"))
            print(f"Lot No.: {lot_no}")  # ผลลัพธ์: 50756
            print(f"Mfg. date: {mfg_date}")  # ผลลัพธ์: 19/05/25
            print(f"Exp. date: {exp_date}", "\n")  # ผลลัพธ์: 19/05/27

            lme = (lot_no, mfg_date, exp_date)
            temp_lme = (self.lot, self.mfg, self.exp)
            for i, w in enumerate(lme if lme else ['', '', '']):
                lmf_label[i].setText(w if w else "XXXXXX")
                if temp_lme[i] != w:
                    statusCheck = False
                    # widget.setStyleSheet("color: rgb(255, 0, 0)")

            return statusCheck
        except Exception as err:
            print(err)
            return False

    # ===== ผลลัพธ์การตรวจสอบ =====
    @Slot(np.ndarray, np.ndarray, str, float)
    def detection_ocr_result(self, processed_image, preprocessed_image, text, processing_time):
        q_img = cvimg_to_qpixmap(processed_image)
        self.detection_view.setPixmap(q_img)

        print("(Camera detected a message)=> ")
        print(f"Processing in: {processing_time:.4f}s")

        try:
            lmf_label: list[QLabel] = [self.lot_detected, self.mfg_detected, self.exp_detected]
            statusCheck = self._parse_lme(text, lmf_label)
            self._update_ui_detection(statusCheck)
            
        except Exception as err:
            pass

    # ===== อัพเดทหน้าจอการตรวจสอบ =====
    def _update_ui_detection(self, statusCheck: bool, isTesting=False):
        initial_style = self.detection_alert.styleSheet()
        if not isTesting:
            if statusCheck:
                self.countOK += 1 
                self.config.update_counter(ok=1)
            else:
                self.countNG += 1
                self.config.update_counter(ng=1)

            self.count_total.setText(f"{self.countOK + self.countNG:,}")
        
        if statusCheck:
            self.count_ok.setText(f"{self.countOK:,}")
            self.detection_alert.setText("OK")
            self.detection_alert.setStyleSheet(f"{initial_style} background-color: rgb(0, 170, 127);")
            self.buzzer.blink(0.1, 0.1, 1, True)
            
        else:
            self.count_ng.setText(f"{self.countNG:,}")
            self.detection_alert.setText("NG")
            self.detection_alert.setStyleSheet(f"{initial_style} background-color: rgb(255, 17, 17);")
            self.buzzer.blink(0.1, 0.1, 5, True)

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
        QApplication.quit() # ปิดโปรแกรมเก่า
        # เปิดโปรแกรมใหม่เป็น process ใหม่
        python = sys.executable
        script = sys.argv[0]  # main.py
        subprocess.Popen([python, script])
        
        
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
