import cv2
import numpy as np

from picamera2 import Picamera2
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QLabel
from resources.ConfigManager import RectangleSettings
from resources.QPixmapUtil import QPixmapUtil
from resources.FramePreprocessor import FramePreprocessor


class CameraView(QThread):
    def __init__(self, monitor: QLabel, camera: Picamera2, rectangle: RectangleSettings, flashLightPin: int):
        super().__init__()
        self.camera = camera
        self.rectangle = rectangle
        self.monitor = monitor
        self.isLiveView = True
        self.isShowRect = False
        self.filtered = False

        self.preprocessor = FramePreprocessor()

        config = self.camera.create_still_configuration(
            main={"size": (1024, 768)},
            buffer_count=4,
            queue=False
        )
        self.camera.configure(config)
        self.camera.start()

        metadata = self.camera.capture_metadata()
        print(f"Current Exposure: {metadata['ExposureTime']}, Gain: {metadata['AnalogueGain']}")

        # เริ่มต้นด้วยค่า default
        self.setCameraControls(
            AeEnable=True,
            ExposureTime=10000,
            AnalogueGain=2,
            AwbEnable=False,
            Brightness=0,
            Contrast=1.8,
            Saturation=1.2,
            Sharpness=1.5,
            FrameRate=25,
            ColourGains=(0, 0),
        )

    # ---------- Method ปรับค่า Controls ----------
    def setCameraControls(self, **kwargs):
        """
        อัปเดตค่าการควบคุมของกล้องตามพารามิเตอร์ที่ส่งเข้ามา

        สามารถเรียกใช้โดยระบุเฉพาะค่าที่ต้องการปรับ เช่น:
            setCameraControls(ExposureTime=20000, AnalogueGain=3.0)

        ฟังก์ชันนี้จะกรองเฉพาะพารามิเตอร์ที่กล้องรองรับ และตรวจสอบช่วงค่าที่เหมาะสมก่อนส่งไปยังกล้อง
        หากมีค่าที่อยู่นอกช่วงหรือไม่รองรับ จะถูกละเว้นโดยอัตโนมัติ

        รองรับการปรับค่าต่อไปนี้:
            - AeEnable: เปิด/ปิด Auto Exposure (True/False)
            - ExposureTime: เวลาชัตเตอร์ (100–1,000,000 µs)
            - AnalogueGain: ค่า gain แบบ manual (1.0–16.0)
            - AwbEnable: เปิด/ปิด Auto White Balance (True/False)
            - Brightness: ความสว่างของภาพ (-1.0 ถึง +1.0)
            - Contrast: ความต่างของภาพ (0.0–16.0)
            - Saturation: ความอิ่มสี (0.0–32.0)
            - Sharpness: ความคมของภาพ (0.0–16.0)
            - FrameRate: เฟรมเรต (1–120 fps)
            - ColourGains: ค่า gain สำหรับ Red และ Blue (0.0–32.0)
            - NoiseReductionMode: โหมดลด noise (0–4)

        หากไม่มีพารามิเตอร์ที่ถูกต้องหรืออยู่ในช่วงที่กำหนด ฟังก์ชันจะไม่ส่งคำสั่งไปยังกล้อง
        """
        valid_keys = {
            "AeEnable", "ExposureTime", "AnalogueGain", "AwbEnable",
            "Brightness", "Contrast", "Saturation", "Sharpness",
            "FrameRate", "ColourGains", "NoiseReductionMode"
        }

        # กรองเฉพาะ key ที่ถูกต้อง
        controls = {k: v for k, v in kwargs.items() if k in valid_keys}

        if not controls:
            print("ไม่มีพารามิเตอร์ที่ถูกต้องสำหรับการอัปเดตกล้อง")
            return

        try:
            self.camera.set_controls(controls)
            print("Camera controls updated:", controls)
        except Exception as e:
            print("Failed to update camera controls:", e)

    # ---------- Toggle live view ----------
    def liveView(self, value: bool):
        self.isLiveView = value

    # ---------- จับภาพ ----------
    def captured(self, showRect: bool = True):
        X1, Y1, X2, Y2 = self.rectangle.X1, self.rectangle.Y1, self.rectangle.X2, self.rectangle.Y2
        frame = self.camera.capture_array()

        if self.isShowRect and showRect:
            cv2.rectangle(frame, (X1, Y1), (X2, Y2), (255, 0, 0), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = np.ascontiguousarray(frame)
        return frame

    # ---------- Thread Loop ----------
    def run(self):
        self.thead_running = True
        try:
            while self.thead_running:
                if self.isLiveView:
                    frame = self.captured()
                    # แปลงเป็น grayscale และทำ preprocessing
                    if self.filtered:
                        frame = self.preprocessor.process(frame)


                    q_img = QPixmapUtil.from_cvimg(frame)
                    self.monitor.setPixmap(q_img)
                QThread.msleep(50)
        except Exception as err:
            self.camera.close()
            print("Camera resources released.")

    # ---------- Close ----------
    def close(self):
        self.thead_running = False
        self.camera.close()
