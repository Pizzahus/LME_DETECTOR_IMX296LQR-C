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

        # self.focus_widget: QLabel = widgets["focus"]
        # self.zoom_widget: QLabel = widgets["zoom"]
        # self.brightness_widget: QLabel = widgets["brightness"]
        # self.contrast_widget: QLabel = widgets["contrast"]
        # self.exposure_widget: QLabel = widgets["exposure"]

        self.updateImage.connect(self._update_pixmap)

    def _mapValue(self, value, min=0, max=255):
        return f"{(((value-min) / (max-min)) * 100):.2f} %"

    @Slot(QPixmap)
    def _update_pixmap(self, pixmap):
        self.monitor.setPixmap(pixmap)

    def liveView(self, value: bool):
        self.isLiveView = value

    def stop_thead(self):
        self.thead_running = False

    def _detect_and_recognize_text(self, image):
        # ใช้ Tesseract OCR อ่านข้อความ
        config = r"--oem 1 --psm 6 -c tessedit_char_whitelist=0123456789/"
        text = pytesseract.image_to_string(image, config=config)

        return text, image

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
            start_time = time()
            # _, thresh = cv2.threshold(cropped_frame, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            text, image = self._detect_and_recognize_text(inverted_image)
            # พิมพ์ข้อความที่อ่านได้
            now = datetime.now()
            timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")
            print(timestamp, "\n", text)

            # จับเวลาที่สิ้นสุด
            end_time = time()
            processing_time = end_time - start_time
            print(f"Processing time => {processing_time:.2f}s\n")

            return text, image

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
        finally:
            if hasattr(self, "picam2"):
                self.camera.close()  # หากใช้ PiCamera ควรปิดการเชื่อมต่อด้วย
            print("Camera resources released.")


class Detector(QThread):
    detectionResults = Signal(numpy.ndarray, bool)
    updateLabel = Signal(numpy.ndarray, object)
    updateImage = Signal(QPixmap)

    def __init__(
        self,
        camera: cv2.VideoCapture,
        widget: dict,
        detection: bool = False,
    ):
        super().__init__()
        self.camera = camera
        self.detection = detection
        self.detection_view: QLabel = widget[0]
        self.lot: QLabel = widget[1]
        self.mfg: QLabel = widget[2]
        self.exp: QLabel = widget[3]
        self.initialLot = self.lot.styleSheet()
        self.initialMfg = self.mfg.styleSheet()
        self.initialExp = self.exp.styleSheet()
        self.updateImage.connect(self.update_detection_view)
        self.updateLabel.connect(self.update_label)

    def filteredText(self, text):
        filtered_text = []

        # ตรวจหาเฉพา index ที่มีเฉพาะตัวเลขและ "/"
        for item in text:
            if all(char.isdigit() or char in "/," for char in item):
                if item:
                    filtered_text.append(item)

        print("(Filter messages detected by the camera)=> ", filtered_text)

        return filtered_text

    def detect(self, image):
        # config = r"--oem 3 --psm 12 -l eng"
        # config = r"--oem 3 --psm 12"
        config = r"--oem 1 --psm 6 -c tessedit_char_whitelist=0123456789/"
        _detect: str = pytesseract.image_to_string(image, config=config)
        results = _detect.split("\n")
        print("(Camera detected a message)=> ", results)

        return results

    @Slot(QPixmap)
    def update_detection_view(self, pixmap):
        self.detection_view.setPixmap(pixmap)

    @Slot(numpy.ndarray, object)
    def update_label(self, image, detect):
        # พิมพ์ข้อความที่ดึงออกมาได้
        widgets: QLabel = [self.lot, self.mfg, self.exp]
        initialStyle = [self.initialLot, self.initialMfg, self.initialExp]
        statusCheck = True

        _detect = [d for d in detect if d]  # กรองเฉพาะค่าที่ไม่ว่าง
        if self.detection:
            settingsRead: dict = self.settingsFile.read()
            settings: dict = settingsRead["lme"]
            lme = list(settings.values())

        for i, w in enumerate(widgets):
            widget: QLabel = w
            try:
                widget.setText(_detect[i])
                if self.detection:
                    if _detect[i] != lme[i]:
                        statusCheck = False
                        widget.setStyleSheet("color: rgb(255, 0, 0)")
                    else:
                        widget.setStyleSheet(initialStyle[i])

            except Exception as e:
                statusCheck = False
                widget.setText("XXXXXX")
                if self.detection:
                    widget.setStyleSheet("color: rgb(255, 0, 0)")

        # ส่งคืนผลการตรวจจับ
        self.detectionResults.emit(image, statusCheck)

    # def run(self):
    #     start_time = time()
    #     # ret, frame = self.camera.read()
    #     # if not ret:
    #     #     print("เกิดข้อผิดพลาดในการจับภาพจากกล้องเว็บแคม")
    #     #     return
    #     frame = self.cap.capture_array()
    #     cv2.rectangle(frame, (X1, Y1), (X2, Y2), (0, 0, 255), 0)  # สีแดง (BGR)

    #     # ครอปเฟรมตามกรอบที่กำหนด
    #     cropped_frame = frame[Y1:Y2, X1:X2]

    #     # กลับสีรูป
    #     inverted_image = cv2.bitwise_not(cropped_frame)

    #     # ใช้ Tesseract เพื่อดึงข้อความจากภาพพร้อมการตั้งค่าที่กำหนด
    #     detect: str = self.detect(inverted_image)
    #     self.updateLabel.emit(inverted_image, detect)

    #     # จับเวลาที่สิ้นสุด
    #     end_time = time()
    #     processing_time = end_time - start_time
    #     print(f"Processing time => {processing_time:.2f}\n")

    #     # Add processing time text to the image
    #     text = f"{processing_time:.2f}s"
    #     font = cv2.FONT_HERSHEY_TRIPLEX
    #     font_scale = 0.4
    #     font_color = (0, 255, 0)
    #     thickness = 1
    #     text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    #     text_x = inverted_image.shape[1] - text_size[0] - 10  # 10 pixels from the right
    #     text_y = text_size[1] + 10  # 10 pixels from the top
    #     cv2.putText(
    #         inverted_image,
    #         text,
    #         (text_x, text_y),
    #         font,
    #         font_scale,
    #         font_color,
    #         thickness,
    #     )

    #     # Convert to QImage
    #     rgb_image = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB)
    #     h, w, ch = rgb_image.shape
    #     bytes_per_line = ch * w
    #     q_image = QImage(
    #         rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888
    #     )
    #     pixmap = QPixmap.fromImage(q_image)

    #     # Update QLabel with the new frame
    #     self.updateImage.emit(pixmap)
    #     QThread.msleep(50)
