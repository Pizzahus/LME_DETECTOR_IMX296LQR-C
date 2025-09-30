import os
import cv2
import numpy as np
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
os.makedirs(os.path.join(capture_dir, "original"), exist_ok=True)
os.makedirs(os.path.join(capture_dir, "process"), exist_ok=True)

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

rectColor = (255, 17, 0)

class CameraView(QThread):
    updateImage = Signal(QPixmap)
    updateDetectImage = Signal()
    ocrResult = Signal(tuple)  # ส่งผลลัพธ์ OCR กลับ

    def __init__(self, monitor: QLabel, camera: Picamera2, sensorPin: int, 
                 rectangle: RectangleSettings, flashLightPin: int, showFps: bool = False):
        super().__init__()
        self.monitor = monitor
        self.camera = camera
        self.sensor = Button(sensorPin, pull_up=True, bounce_time=0.05)
        self.rectangle = rectangle
        # self.flashLight = LED(flashLightPin, active_high=True)
        self.isLiveView = True
        self.is_triggered = False
        self.isShowRect = False
        self.showFps = showFps
        
        # ตัวแปรเพิ่มประสิทธิภาพ
        self.last_frame = None
        self.frame_count = 0
        self.fps_buffer = collections.deque(maxlen=30)
        
        # ตั้งค่ากล้องที่เหมาะสม
        config = self.camera.create_still_configuration(
            main={"size": (1024, 768)}, 
            buffer_count=6,  # เพิ่ม buffer count
            queue=True
        )
        self.camera.configure(config)
        
        # ตั้งค่า controls ที่เหมาะสม
        controls = {
            "AeEnable": True,
            "ExposureTime": 8000,  # ลด exposure time
            "AnalogueGain": 1.5,   # ลด gain
            "AwbEnable": False,
            "Brightness": 0.1,     # ปรับค่าให้เหมาะสม
            "Sharpness": 1.0,      # ลด sharpness เพื่อเพิ่มความเร็ว
            "FrameRate": 90,       # เพิ่ม frame rate
            "Contrast": 1.0,       # ตั้งค่า contrast ปกติ
        }
        self.camera.set_controls(controls)
        
        self.camera.start()
        
        # Pre-compile regex patterns สำหรับ OCR
        self.lot_no_pattern = re.compile(r"\s*\|?\s*(\d{5})")
        self.date_pattern = re.compile(r"\d{2}/\d{2}/\d{2}")
        
        # OCR configuration ที่เหมาะสม
        self.ocr_config = (
            r"--oem 1 --psm 6 "  # ใช้ PSM 8 สำหรับคำเดียว (เร็วขึ้น)
            r"-c tessedit_char_whitelist=0123456789/ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            r" -c classify_bln_numeric_mode=0"
            r" -c textord_min_linesize=0.5"
        )
        
        self.updateImage.connect(self._update_pixmap)

    @Slot(QPixmap)
    def _update_pixmap(self, pixmap):
        self.monitor.setPixmap(pixmap)

    def liveView(self, value: bool):
        self.isLiveView = value

    def _optimize_image_for_ocr(self, image):
        """ปรับปรุงภาพสำหรับ OCR ให้เร็วขึ้น"""
        # ลดขนาดภาพหากใหญ่เกินไป (แต่รักษาอัตราส่วน)
        # h, w = image.shape[:2]
        # if w > 400:  # ลดขนาดหากกว้างกว่า 400px
        #     scale = 400.0 / w
        #     new_w = 400
        #     new_h = int(h * scale)
        #     image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
        
        # แปลงเป็น grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # ใช้ adaptive thresholding แทน Otsu (เร็วกว่าในบางกรณี)
        # gray = cv2.adaptiveThreshold(
        #     gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        #     cv2.THRESH_BINARY, 11, 2
        # )
        
        return gray

    def _detect_and_recognize_text(self, image):
        """ฟังก์ชันตรวจจับและจดจำข้อความที่ปรับปรุงแล้ว"""
        start_time = perf_counter()
        
        # ปรับปรุงภาพสำหรับ OCR
        gray = self._optimize_image_for_ocr(image)
        
        # ใช้ OCR ที่เร็วขึ้น
        try:
            data = pytesseract.image_to_data(
                gray, 
                lang="label",  # ใช้ eng แทน label หากเร็วกว่า
                config=self.ocr_config, 
                output_type=pytesseract.Output.DICT
            )
        except Exception as e:
            print(f"OCR Error: {e}")
            return (gray, datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), 0, (None, None, None))
        
        # กรองผลลัพธ์ที่มีความมั่นใจสูง
        high_conf_indices = [i for i, conf in enumerate(data["conf"]) if int(conf) > 70]
        
        # วาดกรอบเฉพาะข้อความที่มีความมั่นใจสูง
        for i in high_conf_indices:
            text = data["text"][i].strip()
            if text:
                x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                cv2.rectangle(image, (x, y), (x + w, y + h), rectColor, 1)
                
                # วาดกรอบแต่ละตัวอักษร (เฉพาะหากจำเป็นจริงๆ)
                if len(text) > 0:
                    char_width = w / len(text)
                    for j, char in enumerate(text):
                        char_x = int(x + j * char_width)
                        char_w = int(char_width)
                        cv2.rectangle(image, (char_x, y), (char_x + char_w, y + h), rectColor, 1)
        
        # แยกข้อมูล
        text = " ".join([data["text"][i] for i in high_conf_indices])
        
        # ค้นหา Lot No. และวันที่
        lot_no_match = self.lot_no_pattern.search(text)
        lot_no = lot_no_match.group(1) if lot_no_match else None
        
        dates = self.date_pattern.findall(text)
        mfg_date = dates[0] if len(dates) >= 1 else None
        exp_date = dates[1] if len(dates) >= 2 else None
        
        lme = (lot_no, mfg_date, exp_date)
        
        # คำนวณเวลา processing
        processing_time = (perf_counter() - start_time) * 1000
        
        # พิมพ์ผลลัพธ์
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")
        print(f"(Camera detected a message)=> Processing: {processing_time:.2f}ms")
        print(f"Results: {text}")
        print(f"Lot No.: {lot_no}, Mfg: {mfg_date}, Exp: {exp_date}\n")
        
        return (gray, timestamp, processing_time, lme)

    def captured(self, filter=False, isDetect=False):
        """ฟังก์ชันจับภาพที่ปรับปรุงแล้ว"""
        X1, Y1, X2, Y2 = self.rectangle.X1, self.rectangle.Y1, self.rectangle.X2, self.rectangle.Y2
        
        # ใช้การจับภาพแบบ non-blocking
        frame = self.camera.capture_array("main")
        
        if self.isShowRect:
            cv2.rectangle(frame, (X1, Y1), (X2, Y2), (255, 0, 0), 2)
        
        # แปลงและแสดงภาพ
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        height, width, channel = frame_rgb.shape
        bytes_per_line = channel * width
        
        # ใช้ memory view แทนการคัดลอกข้อมูล
        q_img = QImage(
            frame_rgb.data, 
            width, 
            height, 
            bytes_per_line, 
            QImage.Format.Format_BGR888
        )
        
        self.updateImage.emit(QPixmap.fromImage(q_img))
        
        # Crop ภาพเฉพาะพื้นที่ที่ต้องการ
        cropped_frame = frame_rgb[Y1:Y2, X1:X2]
        
        # ประมวลผล OCR หากต้องการ
        if isDetect:
            timestamp = datetime.now().strftime("%d%m%y_%H%M%S")
            gray, timestamp_str, processing_time, lme = self._detect_and_recognize_text(cropped_frame)
            
            # บันทึกภาพ (ทำใน thread แยกหากต้องการ)
            # self._save_image_async(cropped_frame, timestamp)
            
            return timestamp_str, processing_time, lme, cropped_frame  # คืนค่า 4 ค่า
        else:
            return cropped_frame

    def _save_image_async(self, image, timestamp):
        """บันทึกภาพแบบ asynchronous"""
        # สามารถใช้ QThreadPool หรือ threading สำหรับการบันทึกไฟล์
        # เพื่อไม่ให้บล็อก thread หลัก
        def save_task():
            original_path = f"captured_images/original/cap_{timestamp}.png"
            process_path = f"captured_images/process/cap_{timestamp}.png"
            cv2.imwrite(original_path, image)
            # หากต้องการบันทึกภาพที่ประมวลผลแล้ว
            # cv2.imwrite(process_path, processed_image)
        
        # ใช้ QTimer หรือ threading เพื่อรัน save_task แบบไม่บล็อก
        # ตัวอย่างง่ายๆ: threading.Thread(target=save_task, daemon=True).start()
        # แต่ต้อง import threading

    def run(self):
        """เมธอดรันหลักที่ปรับปรุงแล้ว"""
        self.thread_running = True
        last_fps_time = perf_counter()
        
        try:
            while self.thread_running:
                current_time = perf_counter()
                
                if self.isLiveView:
                    # อัพเดท FPS ทุก 1 วินาที
                    if current_time - last_fps_time >= 1.0 and self.showFps:
                        if self.frame_count > 0:
                            fps = self.frame_count / (current_time - last_fps_time)
                            print(f"FPS: {fps:.2f}")
                        last_fps_time = current_time
                        self.frame_count = 0
                    
                    # จับภาพและแสดงผล
                    self.captured()
                    self.frame_count += 1
                    
                else:
                    # ตรวจสอบเซ็นเซอร์
                    if self.sensor.is_pressed and not self.is_triggered:
                        self.is_triggered = True
                        self.updateDetectImage.emit()
                    elif not self.sensor.is_pressed:
                        self.is_triggered = False
                
                # พักสายเล็กน้อยเพื่อไม่ให้ใช้ CPU สูงเกินไป
                self.msleep(5)  # ใช้ msleep ของ QThread แทน time.sleep
                
        except Exception as err:
            print(f"Camera error: {err}")
            if hasattr(self, "camera"):
                self.camera.close()
            print("Camera resources released.")

    def close(self):
        """ปิดทรัพยากร"""
        self.thread_running = False
        self.wait(1000)  # รอ thread สิ้นสุด (สูงสุด 1 วินาที)
        if hasattr(self, "camera"):
            self.camera.close()