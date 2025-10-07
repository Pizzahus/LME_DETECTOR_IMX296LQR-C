import os
import subprocess
import sys
import re
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
from PySide6.QtCore import QMetaObject, Slot, QTimer, QUrl, Qt
from PySide6.QtGui import  QMovie
from PySide6.QtWidgets import QApplication, QWidget
from datetime import datetime
from time import sleep

from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import QProxyStyle, QSlider, QTabBar
from gpiozero import Button, LED, OutputDevice

from resources.ConfigManager import ConfigManager
from resources.Rectangle import Rectangle
from resources.Camera import CameraView, RectangleSettings
from resources.Datetime import ShowDateTime
from resources.Alert import Alert
from resources.Ocr import OcrWorker
from resources.QPixmapUtil import QPixmapUtil
from resources.Rejection import RejectionWorker
from resources.SysInfo import SystemMonitor
from resources.ImageSaverWorker import ImageSaverWorker
# from resources.Animation import AnimatedWidgetHelper

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
GIF_FILE = os.path.join(BASE_DIR, "gui", "assets", "gif", "connecting.gif")

#  Keyboard 
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
os.environ["QT_QPA_PLATFORM"] = "xcb"
qml_path = os.path.join(os.path.dirname(__file__), "keyboard.qml")

# Override QTabBar
class FlatTabStyle(QProxyStyle):
    def drawControl(self, element, option, painter, widget=None):
        if element == QProxyStyle.CE_TabBarTabShape:
            option.shape = QTabBar.RoundedNorth
        super().drawControl(element, option, painter, widget)

class LMEDetect(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

        # ===== ข้อมูลการตั้งค่า pins input, output =====
        pins = self.config.get_gpio_settings() 

        # ===== ข้อมูลการตั้งค่า pins input, output =====
        self.systemSettings = self.config.get_system_settings() 
        self.cameraSettings = self.config.get_camera_settings() 

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
        self.buzzer = LED(pins.BUZZER)

        # =====  rectangle ===== 
        _rectangle = self.config.get_rectangle()
        self.rectangle_margin = 5
        self.rectangle = Rectangle(self.lme_settings_monitor)
        self.rectangle.set_rectangle_from_image_coords(_rectangle)
        self.rectangle.show()  # ต้องเรียก show() เพื่อแสดงวิดเจ็ต
        self.lme_settings_monitor.installEventFilter(self.rectangle)
        self.rectangle.rect_drawn.connect(self.setRectangle)

        # ===== Camera =====
        self.cropped_frame = None
        picam2 = Picamera2()
        self.monitor = self.detection_monitor # หน้าจอแสดง frame
        self.camera = CameraView(monitor=self.monitor, camera=picam2, rectangle=_rectangle, flashLightPin=pins.L0)
        self.camera.start()

        # ===== ImageSaverWorker =====
        self.image_saver = ImageSaverWorker()

        # ===== Queue OCR V1 =====
        self.task_queue = queue.Queue()
        self.ocr_worker = OcrWorker(self.task_queue, angle=90)
        self.ocr_worker.finished.connect(self.detection_ocr_result)
        self.ocr_worker.start()

        # ===== Queue OCR V2 =====
        # self.ocr = OcrWorker()
        # self.ocr.finished.connect(self.detection_ocr_result)

        # ===== Sensor =====
        self.capturedSensor = Button(pin=pins.DI0, pull_up=False, bounce_time=0.02)
        self.capturedSensorDelay = 0
        self.capturedSensor.when_pressed = self._detection
        self.sensorTimer = QTimer()
        self.sensorTimer.timeout.connect(self.checkSensorState)

        # ===== Rejection =====
        self.rejectSensor = Button(pins.DI1, pull_up=False, bounce_time=0.01)
        self.rejector = OutputDevice(pins.DO0, active_high=True, initial_value=False)
        self.rejection = RejectionWorker(sensor=self.rejectSensor, rejector=self.rejector, startReject=3, rejectDelay=0.5)
        self.rejection.rejected_signal.connect(lambda tag: print(f"GUI: {tag} ถูก reject!"))
        self.rejection.start()

        # ===== Alert ===== 
        self.detectionAlert = Alert(self.detection_alert)

        # ===== สร้างและตั้งค่า Virtual Keyboard =====
        self.initalVirtualKeyboard()

        self.configurations()
        # Override QTabBar
        tabBar = self.tabWidget.tabBar()
        tabBar.setStyle(FlatTabStyle())
        tabBar.setStyleSheet("QTabBar::tab { color: #1565C0;}")

        # ===== system mointor =====
        self.sysMonitor = SystemMonitor()
        self.systemMonitor()
        self.sysMonitorTimer = QTimer()
        self.sysMonitorTimer.timeout.connect(self.systemMonitor)

    # ===== system mointor =====
    def systemMonitor(self):
        info = self.sysMonitor.get_all_info()

        cpu_percent = info.get("cpu_percent", 0.0)
        cpu_freq = info.get("cpu_freq", 0.0)
        ram = info.get("ram")
        disk = info.get("disk")
        temperature = info.get("temperature")

        # ป้องกัน format error
        try:
            self.cpu_usage.setText(f"CPU: {float(cpu_percent):.1f}% @ {float(cpu_freq):.0f}MHz")
        except Exception:
            self.cpu_usage.setText("CPU: N/A")

        if ram:
            try:
                used = ram.used / 1024 / 1024
                total = ram.total / 1024 / 1024
                self.ram_usage.setText(f"RAM: {used:.2f}/{int(total)}MB")
            except Exception:
                self.ram_usage.setText("RAM: N/A")
        else:
            self.ram_usage.setText("RAM: N/A")

        if disk:
            try:
                used = disk.used / 1024 / 1024 / 1024
                total = disk.total / 1024 / 1024 / 1024
                self.disk_usage.setText(f"Disk: {used:.2f}/{int(total)}GB")
            except Exception:
                self.disk_usage.setText("Disk: N/A")
        else:
            self.disk_usage.setText("Disk: N/A")

        if temperature is not None:
            try:
                self.cpu_temp.setText(f"Temp: {float(temperature):.1f} C")
            except Exception:
                self.cpu_temp.setText("Temp: N/A")
        else:
            self.cpu_temp.setText("Temp: N/A")

        # IP address
        self.eth0.setText(f"eth0: {self.sysMonitor.get_ip('eth0')}")
        self.eth1.setText(f"eth1: {self.sysMonitor.get_ip('eth1')}")
        self.wlan0.setText(f"wlan0: {self.sysMonitor.get_ip('wlan0')}")

    # ===== ตั้งค่าเริ่มต้น =====
    def configurations(self):
        # ===== ตั้งค่ากล้อง =====
        self.cameraBrightness.setRange(-100, 100)
        self.cameraContrast.setRange(100, 1600)
        self.cameraSaturation.setRange(100, 3200)
        self.cameraAnalogueGain.setRange(100, 1600)
        self.cameraSharpness.setRange(100, 1600)

        sys_cf = self.systemSettings
        cam_cf = self.cameraSettings
        self.save_images_detection.setChecked(sys_cf.saveImage)
        if sys_cf.saveImage:
            self.image_saver.start()

        self.capturedSensorDelay = sys_cf.delayShutter
        self.exposureTime.setText(f"{cam_cf.ExposureTime}")
        self.delayShutter.setText(f"{sys_cf.delayShutter}")
        self.frameRate.setText(f"{cam_cf.FrameRate}")
        self.cameraBrightness.setValue(cam_cf.Brightness * 100)
        self.cameraContrast.setValue(cam_cf.Contrast * 100)
        self.cameraSaturation.setValue(cam_cf.Saturation * 100)
        self.cameraAnalogueGain.setValue(cam_cf.AnalogueGain * 100)
        self.cameraSharpness.setValue(cam_cf.Sharpness * 100)

        self.delayBeforeReject.setText(f"{sys_cf.delayBeforeReject}")
        self.numberStickerBeforeDetection.setText(f"{sys_cf.numberStickerBeforeDetection}")
        self.rejectionPeriod.setText(f"{sys_cf.rejectionPeriod}")
        self.rotateImage.setText(f"{sys_cf.rotateImage}")
        self.detectionPercentage.setText(f"{sys_cf.detectionPercentage}")

        # เชื่อมต่อ Slider
        self.connectSliderToCamera(self.cameraBrightness, "Brightness", scale=0.01)
        self.connectSliderToCamera(self.cameraContrast, "Contrast", scale=0.01)
        self.connectSliderToCamera(self.cameraSaturation, "Saturation", scale=0.01)
        self.connectSliderToCamera(self.cameraAnalogueGain, "AnalogueGain", scale=0.01)
        self.connectSliderToCamera(self.cameraSharpness, "Sharpness", scale=0.01)
        controls = {
            "ExposureTime": cam_cf.ExposureTime,
            "Brightness": cam_cf.Brightness,
            "Contrast": cam_cf.Contrast,
            "Saturation": cam_cf.Saturation,
            "AnalogueGain": cam_cf.AnalogueGain,
            "Sharpness": cam_cf.Sharpness,
            "FrameRate": cam_cf.FrameRate,
        }
        self.camera.setCameraControls(**controls)

        # ตั้งค่า reject
        self.rejection.rejectDelay = sys_cf.delayBeforeReject
        self.rejection.rejectionPeriod = sys_cf.rejectionPeriod

        # ตั้งค่า OCR
        self.ocr_worker.angle = sys_cf.rotateImage
        self.ocr_worker.confidence = sys_cf.detectionPercentage

    # ===== อัพเดทข้อมูลการตั้งค่าเรียวไทม์ =====
    def updateConfigurations(self, key, value):
        if key == "ExposureTime":
            self.camera.setCameraControls(**{key: int(value)})
        elif key == "FrameRate":
            self.camera.setCameraControls(**{key: int(value)})
        elif key == "delayShutter":
            self.capturedSensorDelay = int(value)
        elif key == "delayBeforeReject":
            self.rejection.rejectDelay = int(value)
        elif key == "rejectionPeriod":
            self.rejection.rejectionPeriod = int(value)
        elif key == "rotateImage":
            self.ocr_worker.angle = int(value)
        elif key == "detectionPercentage":
            self.ocr_worker.confidence = int(value)

    # ===== ตั้งค่ากล้อง =====
    def connectSliderToCamera(self, slider: QSlider, control_name: str, scale: float = 1.0):
        """
        เชื่อม QSlider กับการอัปเดตค่ากล้องผ่าน setCameraControls()

        Parameters:
            slider (QSlider): ตัวสไลเดอร์ที่ต้องการเชื่อม
            control_name (str): ชื่อพารามิเตอร์ในกล้อง เช่น 'Brightness', 'Contrast'
            scale (float): ตัวคูณสำหรับแปลงค่าจาก int เป็น float (เช่น 0.01 สำหรับ Brightness)
        """
        def onSliderChanged(value):
            adjusted_value = value * scale
            self.camera.setCameraControls(**{control_name: adjusted_value})
            self.saveConfigValue("hardware.camera", control_name, adjusted_value)
            # print(f"{control_name} updated to:", adjusted_value)

        slider.valueChanged.connect(onSliderChanged)

    # ===== สร้างและตั้งค่า Virtual Keyboard =====
    def initalVirtualKeyboard(self):
        self.kb_overlay = QQuickWidget(self)
        self.kb_overlay.setSource(QUrl.fromLocalFile(qml_path))
        self.kb_overlay.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.kb_overlay.setClearColor(Qt.transparent)
        self.kb_overlay.setAttribute(Qt.WA_TranslucentBackground)
        self.kb_overlay.setAttribute(Qt.WA_AlwaysStackOnTop)
        self.kb_overlay.setGeometry(0, 0, 1024, 600)
        self.kb_overlay.hide()
        self.root_obj = self.kb_overlay.rootObject()

        # ✅ field ที่ไม่มี section/key จะถูกละเว้นตอนบันทึก
        self.input_fields = [
            (self.lot_set,),
            (self.mfg_set,),
            (self.exp_set,),
            (self.delayShutter, "system", "delayShutter"),
            (self.delayBeforeReject, "system", "delayBeforeReject"),
            (self.rejectionPeriod, "system", "rejectionPeriod"),
            (self.numberStickerBeforeDetection, "system", "numberStickerBeforeDetection"),
            (self.rotateImage, "system", "rotateImage"),
            (self.detectionPercentage, "system", "detectionPercentage"),
            (self.exposureTime, "hardware.camera", "ExposureTime"),
            (self.frameRate, "hardware.camera", "FrameRate"),
        ]

        self.tabWidget.currentChanged.connect(self.hideKeyboard)

        # เชื่อม signal จาก QML → ซ่อนคีย์บอร์ด
        if self.root_obj and hasattr(self.root_obj, "reqHideKeyboard"):
            self.root_obj.reqHideKeyboard.connect(self.hideKeyboard)

        # ===== ตั้ง handler ให้ทุก field =====
        for field_info in self.input_fields:
            # ✅ รองรับ tuple ทั้งแบบ 1 และ 3 ค่า
            if len(field_info) == 3:
                field, section, key = field_info
            else:
                field, section, key = field_info[0], None, None

            old_focus_in = field.focusInEvent
            old_focus_out = field.focusOutEvent

            def make_handlers(field, section, key):
                def focus_in(event):
                    self.kb_overlay.show()
                    if self.root_obj and hasattr(self.root_obj, "setActiveField"):
                        self.root_obj.setActiveField(field)
                        # ✅ เก็บ path ไว้ชั่วคราวเพื่อใช้ตอนบันทึก (อาจเป็น None ได้)
                        self.root_obj.setProperty("section", section)
                        self.root_obj.setProperty("key", key)
                    if old_focus_in:
                        old_focus_in(event)

                def focus_out(event):
                    if (
                        self.root_obj
                        and hasattr(self.root_obj, "activeField")
                        and self.root_obj.property("activeField") == field
                    ):
                        self.hideKeyboard()
                    if old_focus_out:
                        old_focus_out(event)

                return focus_in, focus_out

            focus_in, focus_out = make_handlers(field, section, key)
            field.focusInEvent = focus_in
            field.focusOutEvent = focus_out

    # ===== ซ่อน Virtual Keyboard =====
    def hideKeyboard(self):
        # ดึงข้อความสุดท้ายจาก field ปัจจุบัน
        if self.root_obj:
            active_field = self.root_obj.property("activeField")
            if active_field:
                text_value = active_field.text()

                # ค้นหา section, key จาก input_fields
                for field_info in self.input_fields:
                    # แยกแต่ละ tuple ให้ยืดหยุ่น (1 หรือ 3 ค่า)
                    if len(field_info) == 3:
                        field, section, key = field_info
                    else:
                        field, section, key = field_info[0], None, None

                    if field == active_field:
                        if section and key:
                            self.saveConfigValue(section, key, text_value)
                            self.updateConfigurations(key, text_value)
                        break

        # ซ่อน keyboard
        self.kb_overlay.hide()
        self.activateWindow()
        self.setFocus(Qt.OtherFocusReason)
    
    # ===== ฟังก์ชันบันทึกค่าลงไฟล์ configuration.yaml =====
    def saveConfigValue(self, section, key, value):
        # print(f"💾 Saving {section}.{key} = {value}")

        parts = section.split('.')
        target = self.config.config

        for part in parts:
            if part not in target:
                target[part] = {}
            target = target[part]

        # แปลงค่าเป็น int / float ถ้าเหมาะสม
        if isinstance(value, str):
            if value.isdigit():
                value = int(value)
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass

        target[key] = value
        self.config.save_config()

    # ===== เพิ่ม Event ===== 
    def _addEventListener(self):
        self.home_1.clicked.connect(lambda: self._switchToPage(self.detection_page, self.detection_monitor))
        self.home_2.clicked.connect(lambda: self._switchToPage(self.detection_page, self.detection_monitor))
        self.lme_setting_1.clicked.connect(lambda: self._switchToPage(self.lme_settings_page, self.lme_settings_monitor))
        self.lme_setting_2.clicked.connect(lambda: self._switchToPage(self.lme_settings_page, self.lme_settings_monitor))
        self.sys_setting_1.clicked.connect(lambda: self._switchToPage(self.settings_page, self.camera_settings_monitor))
        self.sys_setting_2.clicked.connect(lambda: self._switchToPage(self.settings_page, self.camera_settings_monitor))

        # หน้าตั้งค่า
        self.tabWidget.currentChanged.connect(self.onTabChanged)
        self.camera_filter_1.clicked.connect(self.toggleFilter)
        self.camera_filter_2.clicked.connect(self.toggleFilter)
        self.testReject.clicked.connect(self._testReject)

        # ทดสอบการตรวจจับ
        self.capture_test.clicked.connect(self._test_detection)

        self.capture_set.clicked.connect(self._capTemplateLme)
        self.save_set.clicked.connect(self.setTemplateLme)

        self.save_images_detection.toggled.connect(self._onSaveImageDetection)

        self.shutdown_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.shutdown_page))
        self.shutdown_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.shutdown_page))

        self.start.clicked.connect(self.startDetection)
        self.restart_program_1.clicked.connect(self.restart)
        self.restart_program_2.clicked.connect(self.restart)
        self.cancel_shutdown.clicked.connect(lambda: self.shutdownHandler(False))
        self.confirm_shutdown.clicked.connect(lambda: self.shutdownHandler(True))
        self.count_reset.clicked.connect(self._countReset)

    # ===== บันทึกรูปภาพที่ตรวจจับ ===== 
    def _onSaveImageDetection(self):
        isSaverImage = self.save_images_detection.isChecked()
        self.saveConfigValue("system", "saveImage", isSaverImage)

        if isSaverImage:
            self.image_saver.start()
        else:
            self.image_saver.stop()

    # ===== ทดสอบ sensor (QTimer) ===== 
    def checkSensorState(self):
        capturedSensortriggered = self.capturedSensor.is_pressed
        rejectSensortriggered = self.rejectSensor.is_pressed
        current_index = self.tabWidget.currentIndex()
        if current_index == 2:
            capturedSensorColor = "green" if capturedSensortriggered else "red"
            rejectSensorColor = "green" if rejectSensortriggered else "red"
            self.cameraTriggerSignal.setStyleSheet(f"background-color: {capturedSensorColor};")
            self.rejectTriggerSignal.setStyleSheet(f"background-color: {rejectSensorColor};")

    # ===== เปลี่ยนหน้าต่างแสดงผล ===== 
    def _switchToPage(self, page: QWidget, monitor: QLabel = None):
        self.stackedWidget.setCurrentWidget(page)
        self.currentPage = page
        page_name = page.objectName()
        self.sensorTimer.stop() 
        self.sysMonitorTimer.stop() 

        if monitor:
            self.camera.monitor = monitor
            self.camera.filtered = False
            
        if page_name == "detection_page":
            self.camera.isShowRect = True
        elif page_name == "lme_settings_page":
            template = self.config.get_template()
            _lot = template.lot
            _mfg = template.mfg
            _exp = template.exp

            self.lot_set.setText(_lot)
            self.mfg_set.setText(_mfg)
            self.exp_set.setText(_exp)
            self.camera.isShowRect = False
        elif page_name == "settings_page":
            self.camera.filtered = self.camera_filter_1.isChecked()
            self.camera.isShowRect = False
            self.tabWidget.setCurrentIndex(0)
        else:
            self.camera.isShowRect = False
     
    # ===== เปลี่ยนหน้าต่างแสดงผลในส่วนของหน้าตั้งค่า ===== 
    def onTabChanged(self, tabIndex):
        self.camera.filtered = self.camera_filter_1.isChecked()
        if tabIndex == 0:
            self.sensorTimer.stop() 
            self.sysMonitorTimer.stop() 
            self.camera.monitor = self.camera_settings_monitor
        elif tabIndex == 1:
            self.sensorTimer.stop() 
            self.sysMonitorTimer.stop() 
            self.camera.monitor = self.sys_settings_monitor
        elif tabIndex == 2:
            self.sensorTimer.start(50)  # ตรวจทุก 50 ms
            self.sysMonitorTimer.start(2000)  # ตรวจทุก 50 ms

    # ===== เปิด/ปิด ฟิวเตอร์ ===== 
    def toggleFilter(self):
        self.camera.filtered = self.camera_filter_1.isChecked()

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
            self.camera.rectangle = rect
            self.config.update_rectangle(rect)
        else:
            _X1 = self.camera.rectangle.X1
            _Y1 = self.camera.rectangle.Y1
            _X2 = self.camera.rectangle.X2
            _Y2 = self.camera.rectangle.Y2
            rect = RectangleSettings(X1=_X1, Y1=_Y1, X2=_X2, Y2=_Y2)
            self.rectangle.set_rectangle_from_image_coords(rect)

    # ===== อ่าน lot, mfg, exp จากฉลาก =====
    def _capTemplateLme(self):
        X1 = self.camera.rectangle.X1
        Y1 = self.camera.rectangle.Y1
        X2 = self.camera.rectangle.X2
        Y2 = self.camera.rectangle.Y2
        MARGIN = self.rectangle_margin

        frame = self.camera.captured()
        self.cropped_frame = frame[Y1-MARGIN:Y2-MARGIN, X1-MARGIN:X2-MARGIN]
        original_image, processed_image, preprocessed_image, text, processing_time = self.ocr_worker.detect_and_recognize_text(self.cropped_frame)
        print("(Camera detected a message)=> ")
        print(f"Processing in: {processing_time:.4f}s")
        q_img = QPixmapUtil.from_cvimg(processed_image)
        self.webcam_setting_view.setPixmap(q_img)

        lmf_label: list[QLabel] = [self.lot_set, self.mfg_set, self.exp_set]
        self._parse_lme(text, lmf_label)
    
    # ===== บันทึกการตั้งค่า lot, mfg, exp และ rectangle ===== 
    def setTemplateLme(self):
        lot = self.lot_set.text()
        lot = None if lot == "XXXXXX" else lot

        mfg = self.mfg_set.text()
        mfg = None if mfg == "XXXXXX" else mfg

        exp = self.exp_set.text()
        exp = None if exp == "XXXXXX" else exp

        if lot and mfg and exp:
            print("(Set template lme)=> ", "Lot", lot, "Mfg", mfg, "Exp", exp)
            self.lot = lot
            self.mfg = mfg
            self.exp = exp
            self.config.update_template(lot, mfg, exp)

    # ===== เริ่มการตรวจจับ ===== 
    def startDetection(self):
        isRunning = self.start.isChecked()
        self.camera.liveView(not isRunning)
        self.lme_setting_1.setHidden(isRunning)
        self.lme_setting_2.setHidden(isRunning)
        self.sys_setting_1.setHidden(isRunning)
        self.sys_setting_2.setHidden(isRunning)
        self.capture_test.setHidden(isRunning)

        if isRunning:
            self.start.setText("STOP")
            self.detection_status.setText("เริ่มการตรวจจับ")
        else:
            self.start.setText("START")
            self.detection_status.setText("กดปุ่ม START เพื่อเริ่มทำงาน")

    # ===== ทดสอบตรวจจับการพิมพ์ ===== 
    def _test_detection(self):
        X1 = self.camera.rectangle.X1
        Y1 = self.camera.rectangle.Y1
        X2 = self.camera.rectangle.X2
        Y2 = self.camera.rectangle.Y2
        MARGIN = self.rectangle_margin

        frame = self.camera.captured()
        self.cropped_frame = frame[Y1-MARGIN:Y2-MARGIN, X1-MARGIN:X2-MARGIN]
        original_image, processed_image, preprocessed_image, text, processing_time = self.ocr_worker.detect_and_recognize_text(self.cropped_frame)
        print("(Camera detected a message)=> ")
        print(f"Processing in: {processing_time:.4f}s")
        q_img = QPixmapUtil.from_cvimg(processed_image)
        self.detection_view.setPixmap(q_img)

        lmf_label: list[QLabel] = [self.lot_detected, self.mfg_detected, self.exp_detected]
        statusCheck = self._parse_lme(text, lmf_label)
        self._update_ui_detection(statusCheck, isTesting=True)

    # ===== ตรวจจับการพิมพ์ ===== 
    def _detection(self, triggered=True):
        isRunning = self.start.isChecked()
        if triggered and isRunning:
            # ส่งกลับเข้า main thread เพื่อใช้ QTimer ได้
            QMetaObject.invokeMethod(
                self,
                "_delayed_detection",
                Qt.QueuedConnection
            )

    @Slot()
    def _delayed_detection(self):
        QTimer.singleShot(int(self.capturedSensorDelay), self._perform_detection)


    def _perform_detection(self):
        # self.buzzer.blink(0.1, 0.1, 1, True)  # ถ้าต้องการให้ทำงานหลัง delay

        X1 = self.camera.rectangle.X1
        Y1 = self.camera.rectangle.Y1
        X2 = self.camera.rectangle.X2
        Y2 = self.camera.rectangle.Y2
        MARGIN = self.rectangle_margin

        frame = self.camera.captured()
        q_img = QPixmapUtil.from_cvimg(frame)
        self.monitor.setPixmap(q_img)

        self.cropped_frame = frame[Y1-MARGIN:Y2-MARGIN, X1-MARGIN:X2-MARGIN]
        self.task_queue.put(self.cropped_frame)  # version 1 แบบ Queue + QThread
        # self.ocr.run_ocr(self.cropped_frame)  # version 2 แบบ ThreadPoolExecutor

    # ===== ตรวจสอบความถูกต้อง Lot / MFG / EXP =====
    def _parse_lme(self, text: str, lmf_label: list[QLabel]):
        statusCheck = True

        try:
            # หา Lot No. → ตัวเลข 5 หลัก
            length_lot = len(self.lot)
            pattern = rf"\b(\d{{{5}}})\b"  # ค้นหาตัวเลขจำนวน length_lot ที่เป็นคำเต็ม
            lot_match = re.search(pattern, text)
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
    def detection_ocr_result(self, original_image, processed_image, preprocessed_image, text, processing_time):
        q_img = QPixmapUtil.from_cvimg(processed_image)
        self.detection_view.setPixmap(q_img)

        print("(Camera detected a message)=> ")
        print(f"Processing in: {processing_time:.4f}s")

        try:
            lmf_label: list[QLabel] = [self.lot_detected, self.mfg_detected, self.exp_detected]
            statusCheck = self._parse_lme(text, lmf_label)
            self._update_ui_detection(statusCheck)

            if self.save_images_detection.isChecked():
                self.image_saver.put(original_image, statusCheck, self.lot)

        except Exception as err:
            pass

    # ===== อัพเดทหน้าจอการตรวจสอบ และ Reject =====
    def _update_ui_detection(self, statusCheck: bool, isTesting=False):
        initial_style = self.detection_alert.styleSheet()
        if not isTesting:
            if statusCheck:
                self.countOK += 1 
                self.config.update_counter(ok=1)
            else:
                self.countNG += 1
                self.config.update_counter(ng=1)

            # เพิ่ม queue ใน rejection
            totalCount = self.countOK + self.countNG
            self.rejection.put_task(f"Item {totalCount:,}", "OK" if statusCheck else "NG")
            self.count_total.setText(f"{totalCount:,}")
        
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

    # ===== ทดสอบ Reject =====
    def _testReject(self):
        isActive = self.testReject.isChecked()
        if isActive: 
            self.rejector.on()
        else:
            self.rejector.off()

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
        if shutdown:
            print("*** Shutting down")
            sleep(1)
            os.system("sudo poweroff")
        elif not shutdown:
            self._switchToPage(self.currentPage)

    # ปิดโปรแกรม
    def closeEvent(self, event):
        self.buzzer.off()
        self.rejector.off()
        self.image_saver.stop()
        self.sensorTimer.stop()
        self.camera.close()
        self.showDateTime.stop()
        self.ocr_worker.stop()
        self.rejection.stop()
        super().closeEvent(event)
