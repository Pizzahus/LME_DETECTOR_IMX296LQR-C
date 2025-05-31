import os
import cv2
import numpy
import pytesseract
import re

from picamera2 import Picamera2
from gpiozero import Button, LED
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Slot, Signal
from time import time, sleep, perf_counter
from datetime import datetime
from dataclasses import dataclass
import collections
from resources.ConfigManager import ConfigManager, RectangleSettings

# กำหนดโฟลเดอร์ที่จะเก็บภาพ
capture_dir = "./captured_images"
os.makedirs(capture_dir, exist_ok=True)  # สร้างโฟลเดอร์หากยังไม่มี

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

rectColor = (255, 17, 0)


# แสดงภาพจากกล้อง
class CameraView(QThread):
    updateImage = Signal(QPixmap)
    updateDetectImage = Signal()

    def __init__(self, monitor: QLabel, camera: Picamera2, sensorPin: int, rectangle: RectangleSettings, flashLightPin: int, showFps: bool = False):
        super().__init__()
        self.monitor = monitor
        self.camera = camera
        self.sensor = Button(sensorPin, pull_up=True, bounce_time=0.05)  # ตั้งค่า bounce_time = 0.1 วินาที
        self.rectangle = rectangle
        # self.flashLight = LED(flashLightPin, active_high=True)  # ตั้งค่า LED ให้ทำงานแบบ active low
        self.isLiveView = True
        self.is_triggered = False
        self.isShowRect = False
        self.showFps = showFps

        # config = self.camera.create_still_configuration(main={"size": (1024, 768)}, buffer_count=4, queue=False)
        config = self.camera.create_still_configuration(main={"size": (1024, 768)}, buffer_count=4, queue=False)
        self.camera.configure(config)
        self.camera.start()

        # วัดแสงก่อนถ่ายภาพจริง (Optional)
        metadata = self.camera.capture_metadata()
        print(f"Current Exposure: {metadata['ExposureTime']}, Gain: {metadata['AnalogueGain']}")

        # ปิด Auto Exposure และตั้งค่า ExposureTime, AnalogueGain คงที่
        controls = {
            # พารามิเตอร์พื้นฐาน
            "AeEnable": False,
            "ExposureTime": 500,
            "AnalogueGain": 1.4,
            "AwbEnable": False,
            "Brightness": 0.1,
            # "Contrast": 1.8,
            # "Saturation": 1.2,
            # พารามิเตอร์เพิ่มประสิทธิภาพ
            "Sharpness": 1.5,
            "FrameRate": 60,
            # "NoiseReductionMode": "HighQuality",
            # พารามิเตอร์แสง
            # "ColourGains": (1.8, 1.5),
            # "AeMeteringMode": "CentreWeighted"
        }
        self.camera.set_controls(controls)

        # อัพเดท monitor
        self.updateImage.connect(self._update_pixmap)

    # แปลงค่าเป็นเปอร์เซ็นต์
    def _mapValue(self, value, min=0, max=255):
        return f"{(((value-min) / (max-min)) * 100):.2f} %"

    @Slot(QPixmap)  # อัพเดท monitor
    def _update_pixmap(self, pixmap):
        self.monitor.setPixmap(pixmap)

    @Slot(QPixmap)  # อัพเดท detect monitor
    def _update_detect_pixmap(self, pixmap):
        self.monitor.setPixmap(pixmap)

    # ตั้งค่าให้แสดงภาพสด
    def liveView(self, value: bool):
        self.isLiveView = value

    # ตั้งค่าให้แสดงภาพที่จับได้
    def _detect_and_recognize_text(self, image):
        start_time = time()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # ใช้ Pytesseract อ่านข้อความ OCR พร้อมตำแหน่ง
        config = r"--oem 1 --psm 6 -c tessedit_char_whitelist=0123456789/ tessedit_char_blacklist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        data = pytesseract.image_to_data(gray, lang="arial", config=config, output_type=pytesseract.Output.DICT)

        # วาดกรอบรอบข้อความ
        # for i in range(len(data["text"])):
        #     text = data["text"][i]
        #     if text.strip():  # ข้ามข้อความว่าง
        #         x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
        #         cv2.rectangle(image, (x, y), (x + w, y + h), rectColor, 1)
        #         cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, rectColor, 1)

                # วาดกรอบรอบข้อความ
        for i in range(len(data["text"])):
            text = data["text"][i]
            if text.strip():  # ข้ามข้อความว่าง
                x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                
                # คำนวณความกว้างของแต่ละตัวอักษรโดยประมาณ
                char_width = w / len(text)
                
                # ตีกรอบแต่ละตัวอักษร
                for j, char in enumerate(text):
                    char_x = int(x + j * char_width)
                    char_w = int(char_width)
                    
                    # วาดกรอบรอบตัวอักษร
                    cv2.rectangle(image, (char_x, y), (char_x + char_w, y + h), rectColor, 1)
                    
                    # วาดตัวอักษร (optional)
                    cv2.putText(image, char, (char_x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, rectColor, 1)

        # ดึงข้อความมาใช้งานต่อ
        text = " ".join(data["text"])

        # ค้นหา Lot No.
        lot_no = re.search(r"\s*\|?\s*(\d{5})", text)
        lot_no = lot_no.group(1) if lot_no else None

        # ค้นหา MFG / EXP
        dates = re.findall(r"\d{2}/\d{2}/\d{2}", text)
        mfg_date = dates[0] if len(dates) >= 1 else None
        exp_date = dates[1] if len(dates) >= 2 else None

        lme = (lot_no, mfg_date, exp_date)

        # จับเวลาที่สิ้นสุด
        end_time = time()
        processing_time = (end_time - start_time) * 1000

        # พิมพ์ข้อความที่อ่านได้
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")
        print("(Camera detected a message)=> ")
        print(f"Processing in: {processing_time:.2f}ms")
        print("Timestamp: ", timestamp)
        print("Results: ", text.split("\n"))
        print(f"Lot No.: {lot_no}")  # ผลลัพธ์: 50756
        print(f"Mfg. date: {mfg_date}")  # ผลลัพธ์: 19/05/25
        print(f"Exp. date: {exp_date}", "\n")  # ผลลัพธ์: 19/05/27
        return (timestamp, processing_time, lme)

    # ฟังก์ชันจับภาพ
    def captured(self, isDetect=False):
        X1 = self.rectangle.X1
        Y1 = self.rectangle.Y1
        X2 = self.rectangle.X2
        Y2 = self.rectangle.Y2
        frame = self.camera.capture_array()

        if self.isShowRect:
            cv2.rectangle(frame, (X1, Y1), (X2, Y2), (255, 0, 0), 2)

        # Convert color space and ensure the array is contiguous
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = numpy.ascontiguousarray(frame)  # This ensures C-contiguous memory layout
        
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

        # Crop image
        cropped_frame = frame[Y1:Y2, X1:X2]
        # inverted_image = cv2.bitwise_not(cropped_frame)

        # Detect and recognize text
        if isDetect:
            timestamp = datetime.now().strftime("%d%m%y_%H%M%S")
            image_filename = f"captured_images/cap_.png"
            cv2.imwrite(image_filename, cropped_frame)
            timestamp, processing_time, text = self._detect_and_recognize_text(cropped_frame)
            return timestamp, processing_time, text, cropped_frame
        else:
            return cropped_frame

    # ฟังก์ชันจับภาพและบันทึกลงไฟล์
    def saveCapturedImage(self, image, filename):
        # บันทึกภาพที่จับได้ลงในโฟลเดอร์ที่กำหนด
        filepath = os.path.join(capture_dir, filename)
        cv2.imwrite(filepath, image)
        print(f"Image saved: {filepath}")

    # เริ่มการทำงานของกล้อง
    def run(self):
        self.thead_running = True
        frame_times = collections.deque(maxlen=60)  # เก็บเวลา 60 เฟรมล่าสุด
        try:
            while self.thead_running:
                if self.isLiveView:
                    self.captured()

                    if self.showFps:
                            # โค้ดประมวลผลเฟรมของคุณที่นี่
                        frame_times.append(time.perf_counter())
                        
                        if len(frame_times) > 1:
                            # คำนวณ FPS จากเฟรมล่าสุด
                            fps = len(frame_times) / (frame_times[-1] - frame_times[0])
                            print(f"FPS: {fps:.2f}")
                elif self.sensor.is_pressed and not self.is_triggered:
                    self.is_triggered = True
                    # QThread.msleep(100)
                    # sleep(0.2)
                    self.updateDetectImage.emit()
                elif not self.sensor.is_pressed:  # ตรวจสอบสถานะปุ่มแบบ polling
                    self.is_triggered = False

                QThread.msleep(10)
        except Exception as err:
            if hasattr(self, "picam2"):
                self.camera.close()  # หากใช้ PiCamera ควรปิดการเชื่อมต่อด้วย
            print("Camera resources released.")

    def close(self):
        self.thead_running = False
        self.camera.close()
