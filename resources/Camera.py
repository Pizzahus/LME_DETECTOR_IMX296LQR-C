import cv2
import numpy as np

from picamera2 import Picamera2
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QLabel
from time import time
import collections
from resources.ConfigManager import RectangleSettings
from resources.QPixmapUtil import QPixmapUtil

# แสดงภาพจากกล้อง
class CameraView(QThread):
    def __init__(self, monitor: QLabel, camera: Picamera2, rectangle: RectangleSettings, flashLightPin: int, showFps: bool = False):
        super().__init__()
        self.camera = camera
        self.rectangle = rectangle
        self.monitor = monitor
        # self.flashLight = LED(flashLightPin, active_high=True)  # ตั้งค่า LED ให้ทำงานแบบ active low
        self.isLiveView = True
        self.isShowRect = False
        self.showFps = showFps

        config = self.camera.create_still_configuration(main={"size": (1024, 768)}, buffer_count=2, queue=False)
        self.camera.configure(config)

        self.camera.start()

        # วัดแสงก่อนถ่ายภาพจริง (Optional)
        metadata = self.camera.capture_metadata()
        print(f"Current Exposure: {metadata['ExposureTime']}, Gain: {metadata['AnalogueGain']}")

        # ปิด Auto Exposure และตั้งค่า ExposureTime, AnalogueGain คงที่
        controls = {
            # พารามิเตอร์พื้นฐาน
            "AeEnable": True,
            "ExposureTime": 10000,
            "AnalogueGain": 2,
            "AwbEnable": False,
            "Brightness": 0,
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

    # ตั้งค่าให้แสดงภาพสด
    def liveView(self, value: bool):
        self.isLiveView = value

    # ฟังก์ชันจับภาพ
    def captured(self):
        X1 = self.rectangle.X1
        Y1 = self.rectangle.Y1
        X2 = self.rectangle.X2
        Y2 = self.rectangle.Y2
        frame = self.camera.capture_array()

        if self.isShowRect:
            cv2.rectangle(frame, (X1, Y1), (X2, Y2), (255, 0, 0), 2)

        # Convert color space and ensure the array is contiguous
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = np.ascontiguousarray(frame)  # This ensures C-contiguous memory layout
        return frame

    # เริ่มการทำงานของกล้อง
    def run(self):
        self.thead_running = True
        frame_times = collections.deque(maxlen=60)  # เก็บเวลา 60 เฟรมล่าสุด
        try:
            while self.thead_running:
                if self.isLiveView:
                    frame = self.captured()
                    q_img = QPixmapUtil.from_cvimg(frame)
                    self.monitor.setPixmap(q_img)

                    if self.showFps:
                        # โค้ดประมวลผลเฟรมของคุณที่นี่
                        frame_times.append(time.perf_counter())
                        
                        if len(frame_times) > 1:
                            # คำนวณ FPS จากเฟรมล่าสุด
                            fps = len(frame_times) / (frame_times[-1] - frame_times[0])
                            print(f"FPS: {fps:.2f}")

                QThread.msleep(0.05)
        except Exception as err:
            if hasattr(self, "picam2"):
                self.camera.close()  # หากใช้ PiCamera ควรปิดการเชื่อมต่อด้วย
            print("Camera resources released.")

    def close(self):
        self.thead_running = False
        self.camera.close()
        self.wait()
