import cv2
import numpy as np

from picamera2 import Picamera2
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QLabel
from resources.ConfigManager import RectangleSettings
from resources.QPixmapUtil import QPixmapUtil


class CameraView(QThread):
    def __init__(self, monitor: QLabel, camera: Picamera2, rectangle: RectangleSettings, flashLightPin: int):
        super().__init__()
        self.camera = camera
        self.rectangle = rectangle
        self.monitor = monitor
        self.isLiveView = True
        self.isShowRect = False

        config = self.camera.create_still_configuration(
            main={"size": (1024, 768)},
            buffer_count=2,
            queue=True
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
            FrameRate=60,
            ColourGains=(1.8, 1.5),
        )

    # ---------- Method ปรับค่า Controls ----------
    # ---------- Method ปรับค่า Controls ----------
    def setCameraControls(self,
                          AeEnable=False,          # เปิด/ปิด Auto Exposure (True=เปิด, False=ปิด)
                          ExposureTime=10000,      # เวลาชัตเตอร์ (microseconds) ใช้เมื่อ AeEnable=False
                          AnalogueGain=2.0,        # ค่า gain แบบ manual (ใช้เมื่อ AeEnable=False)
                          AwbEnable=False,         # เปิด/ปิด Auto White Balance
                          Brightness=0.0,          # ความสว่าง (-1.0 ถึง +1.0 ประมาณ)
                          Contrast=1.8,            # ความต่างของภาพ (1.0=default, >1=ชัดขึ้น)
                          Saturation=1.2,          # ความอิ่มสี (1.0=ปกติ, >1=สดขึ้น)
                          Sharpness=1.5,           # ความคม (1.0=default)
                          FrameRate=60,            # เฟรมเรต (fps) ต้องสอดคล้องกับ ExposureTime
                          ColourGains=(1.8, 1.5),  # (Red, Blue) gain สำหรับ white balance แบบ manual
                          NoiseReductionMode=0,    # โหมดลด noise 0-4
                          ):
        """
        อัปเดตค่า controls ของกล้อง
        เช่น setCameraControls(ExposureTime=20000, AnalogueGain=3)
        """
        controls = {}

        if AeEnable is not None: controls["AeEnable"] = AeEnable
        if ExposureTime is not None: controls["ExposureTime"] = ExposureTime
        if AnalogueGain is not None: controls["AnalogueGain"] = AnalogueGain
        if AwbEnable is not None: controls["AwbEnable"] = AwbEnable
        if Brightness is not None: controls["Brightness"] = Brightness
        if Contrast is not None: controls["Contrast"] = Contrast
        if Saturation is not None: controls["Saturation"] = Saturation
        if Sharpness is not None: controls["Sharpness"] = Sharpness
        if FrameRate is not None: controls["FrameRate"] = FrameRate
        if ColourGains is not None: controls["ColourGains"] = ColourGains
        if NoiseReductionMode is not None: controls["NoiseReductionMode"] = NoiseReductionMode

        try:
            self.camera.set_controls(controls)
            print("Camera controls updated:", controls)
        except Exception as e:
            print("Failed to update camera controls:", e)


    # ---------- Toggle live view ----------
    def liveView(self, value: bool):
        self.isLiveView = value

    # ---------- จับภาพ ----------
    def captured(self):
        X1, Y1, X2, Y2 = self.rectangle.X1, self.rectangle.Y1, self.rectangle.X2, self.rectangle.Y2
        frame = self.camera.capture_array()

        if self.isShowRect:
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
                    q_img = QPixmapUtil.from_cvimg(frame)
                    self.monitor.setPixmap(q_img)
                QThread.msleep(10)
        except Exception as err:
            self.camera.close()
            print("Camera resources released.")

    # ---------- Close ----------
    def close(self):
        self.thead_running = False
        self.camera.close()
