import os
import cv2
import numpy
import pytesseract

from picamera2 import Picamera2
from gpiozero import Button
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Slot, Signal
from time import time
from datetime import datetime

X1, Y1, X2, Y2 = 230, 300, 550, 450

# กำหนดโฟลเดอร์ที่จะเก็บภาพ
capture_dir = "./captured_images"
os.makedirs(capture_dir, exist_ok=True)  # สร้างโฟลเดอร์หากยังไม่มี

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


# แสดงภาพจากกล้อง
class CameraView(QThread):
    updateImage = Signal(QPixmap)
    updateSettingValue = Signal(QLabel, int, int, int, int)

    def __init__(self, monitor: QLabel, camera: Picamera2, sensorPin: int):
        super().__init__()
        self.monitor = monitor
        self.camera = camera
        self.sensor = Button(sensorPin, pull_up=True, bounce_time=0.05)  # ตั้งค่า bounce_time = 0.1 วินาที
        self.isLiveView = True
        self.is_triggered = False

        config = self.camera.create_still_configuration(main={"size": (1024, 768)}, buffer_count=4)
        self.camera.configure(config)
        self.camera.start()
        # ตั้งค่า Exposure
        self.camera.set_controls({"AeEnable": False, "ExposureTime": 5000, "AnalogueGain": 8.0})  # ปิด Auto Exposure

        # อัพเดท monitor
        self.updateImage.connect(self._update_pixmap)

    def _mapValue(self, value, min=0, max=255):
        return f"{(((value-min) / (max-min)) * 100):.2f} %"

    @Slot(QPixmap)  # อัพเดท monitor
    def _update_pixmap(self, pixmap):
        self.monitor.setPixmap(pixmap)

    def liveView(self, value: bool):
        self.isLiveView = value

    def _detect_and_recognize_text(self, image):
        start_time = time()

        # ใช้ EasyOCR อ่านข้อความ
        config = r"--oem 1 --psm 6 -c tessedit_char_whitelist=0123456789/"
        text = pytesseract.image_to_string(image, config=config)
        results = text.split("\n")
        
        # ลบข้อความที่ว่างหรือไม่ใช่ตัวเลข/วันที่
        text = [line.strip() for line in results if line.strip()]

        # จับเวลาที่สิ้นสุด
        end_time = time()
        processing_time = (end_time - start_time) * 1000

        # พิมพ์ข้อความที่อ่านได้
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")
        print("(Camera detected a message with EasyOCR)=> ")
        print(f"Processing in: {processing_time:.2f}ms")
        print("Timestamp: ", timestamp)
        print("Results: ", text, "\n")
        return (timestamp, processing_time, text)

    def captured(self, isDetect=False):
        text = None
        image = None

        frame = self.camera.capture_array()
        cv2.rectangle(frame, (X1, Y1), (X2, Y2), (255, 0, 0), 2)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        height, width, channel = frame.shape
        bytes_per_line = channel * width
        q_img = QImage(
            frame.data,
            width,
            height,
            bytes_per_line,
            QImage.Format.Format_BGR888,
        )
        self.updateImage.emit(QPixmap.fromImage(q_img))

        # ย่อภาพ
        cropped_frame = frame[Y1:Y2, X1:X2]
        inverted_image = cv2.bitwise_not(cropped_frame)

        # ตรวจจับและอ่านข้อความ
        if isDetect:
            # _, thresh = cv2.threshold(cropped_frame, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            timestamp, processing_time, text = self._detect_and_recognize_text(inverted_image)
            return timestamp, processing_time, text, inverted_image

    def run(self):
        self.thead_running = True
        try:
            while self.thead_running:
                if self.isLiveView:
                    self.captured()
                elif self.sensor.is_pressed and not self.is_triggered:
                    self.is_triggered = True
                    self.captured(True)
                elif not self.sensor.is_pressed:  # ตรวจสอบสถานะปุ่มแบบ polling
                    self.is_triggered = False

                QThread.msleep(50)
        except Exception as err:
            if hasattr(self, "picam2"):
                self.camera.close()  # หากใช้ PiCamera ควรปิดการเชื่อมต่อด้วย
            print("Camera resources released.")

    def close(self):
        self.thead_running = False
        self.camera.close()