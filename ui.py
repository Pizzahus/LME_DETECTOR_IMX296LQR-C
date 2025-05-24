import os
import cv2
from picamera2 import Picamera2

from src.ui_DETECTOR_10inch import Ui_MainWindow
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
)
from PySide6.QtCore import QTimer, Signal, Slot
from PySide6.QtGui import QImage, QPixmap, QMovie
from datetime import datetime
from time import sleep

from resources.WiFi import WiFi
from resources.Keyboard import Keyboard
from resources.Camera import CameraView
from resources.Datetime import ShowDateTime
from resources.Alert import Alert, BUZZER
# from resources.Animation import AnimatedWidgetHelper

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
SAVE_IMAGES_DIR = os.path.join(BASE_DIR, "captured_images")  # โฟล์เดอร์สำหรับบันทึกภาพ
os.makedirs(SAVE_IMAGES_DIR, exist_ok=True)
GIF_FILE = os.path.join(BASE_DIR, "gui", "assets", "gif", "connecting.gif")


class LMEDetect(QMainWindow, Ui_MainWindow):
    def __init__(self, os_name="Windows"):
        """
        token = google.auth.token
        credentials = google.oauth2.credentials.Credentials
        settings = ไฟล์ตั้งค่าโปรแกรม **/files/settings.json
        balancePort = พอร์ต RS232 ** Windows("COM6"), Linux("/dev/ttyUSB0")
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
        self.addEventListener()

        picam2 = Picamera2()
        self.cameraView = CameraView(monitor=self.webcam_monitor, camera=picam2, sensorPin=23, flashLightPin=24)
        self.cameraView.start()

        # self.animator = AnimatedWidgetHelper(self)

    # เพิ่ม Event
    def addEventListener(self):
        self.home_1.clicked.connect(lambda: self.switchToPage(self.detection_page, self.webcam_monitor))
        self.home_2.clicked.connect(lambda: self.switchToPage(self.detection_page, self.webcam_monitor))
        self.setting_1.clicked.connect(lambda: self.switchToPage(self.lme_settings_page, self.webcam_setting_monitor))
        self.setting_2.clicked.connect(lambda: self.switchToPage(self.lme_settings_page, self.webcam_setting_monitor))
        self.camera_setting_1.clicked.connect(lambda: self.switchToPage(self.camera_setting_page, self.camera_setting_monitor))
        self.camera_setting_2.clicked.connect(lambda: self.switchToPage(self.camera_setting_page, self.camera_setting_monitor))

        self.capture_set.clicked.connect(self.setTemplateLme)

        self.shutdown_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.shutdown_page))
        self.shutdown_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.shutdown_page))

        self.start.clicked.connect(self.startDetection)
        self.capture_test.clicked.connect(self.testDetection)
        self.restart_program_1.clicked.connect(self.restart)
        self.restart_program_2.clicked.connect(self.restart)
        self.cancel_shutdown.clicked.connect(lambda: self.shutdownHandler(False))
        self.confirm_shutdown.clicked.connect(lambda: self.shutdownHandler(True))
        self.count_reset.clicked.connect(self._countReset)

    # เปลี่ยนหน้าต่างแสดงผล
    def switchToPage(self, page: QWidget, monitor: QLabel = None):
        self.stackedWidget.setCurrentWidget(page)
        self.currentPage = page
        page_name = page.objectName()
        if monitor:
            self.cameraView.monitor = monitor

    # ตั้งค่า lot, mfg, exp
    def setTemplateLme(self):
        timestamp, processing_time, lme, image = self.cameraView.captured(isDetect=True)
        height, width, channel = image.shape
        bytes_per_line = channel * width

        # Add processing time text to the image
        text = f"{timestamp:s} {processing_time:.2f}ms"
        font = cv2.FONT_HERSHEY_TRIPLEX
        font_scale = 0.5
        font_color = (0, 0, 255)  # BGR
        thickness = 1
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = int((width - text_size[0]) / 2)  # center
        text_y = height - 5  # 5 pixels from the bottom
        cv2.putText(
            image,
            text,
            (text_x, text_y),
            font,
            font_scale,
            font_color,
            thickness,
        )

        q_image = QImage(
            image.data,
            width,
            height,
            bytes_per_line,
            QImage.Format.Format_BGR888,
        )
        self.webcam_setting_view.setPixmap(QPixmap.fromImage(q_image))

        lmf_label: list[QLabel] = [self.lot_set, self.mfg_set, self.exp_set]
        for i, w in enumerate(lme if lme else ['', '', '']):
            lmf_label[i].setText(w if w else "XXXXXX")

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

    # ทดสอบการตรวจจับ
    def testDetection(self):
        self.cameraView.captured(True)

    # รีเซ็ต counter
    def _countReset(self):
        self.countOK = 0
        self.countNG = 0
        self.countTotal = 0
        self.count_ok.setText(str(self.countOK))
        self.count_ng.setText(str(self.countNG))
        self.count_total.setText(str(self.countTotal))
        self.settingsFile.update("countOK", 0)
        self.settingsFile.update("countNG", 0)

        self.settingsFile.update("countTotal", 0)
    
    # รีสตาร์ทโปรแกรม
    def restart(self):
        """รีสตาร์ทโปรแกรม"""
        QApplication.quit()

    # จัดการการปิดเครื่อง
    def shutdownHandler(self, shutdown=True):
        if shutdown and self.os_name == "Linux":
            print("*** Shutting down")
            sleep(1)
            os.system("sudo poweroff")
        elif not shutdown:
            self.switchToPage(self.currentPage)

    # ปิดโปรแกรม
    def closeEvent(self, event):
        self.cameraView.close()
        self.showDateTime.stop()
        super().closeEvent(event)
