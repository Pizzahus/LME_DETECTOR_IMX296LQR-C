import sys
import cv2
import numpy as np
from picamera2 import Picamera2
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QSlider, QGroupBox, QFormLayout
)

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

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Realtime Camera Adjust — Picamera2 + PySide6")
        self.resize(1000, 700)

        # กล้อง
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_preview_configuration(main={"size": (640, 480)}))
        self.picam2.start()

        # Preview
        self.lbl_preview = QLabel("กำลังโหลดกล้อง...")
        self.lbl_preview.setAlignment(Qt.AlignCenter)

        # --- Sliders ---
        self.slider_brightness = QSlider(Qt.Horizontal)
        self.slider_brightness.setRange(-100, 100)
        self.slider_brightness.setValue(0)

        self.slider_contrast = QSlider(Qt.Horizontal)
        self.slider_contrast.setRange(-100, 100)
        self.slider_contrast.setValue(0)

        self.slider_saturation = QSlider(Qt.Horizontal)
        self.slider_saturation.setRange(0, 200)
        self.slider_saturation.setValue(100)

        self.slider_hue = QSlider(Qt.Horizontal)
        self.slider_hue.setRange(-180, 180)
        self.slider_hue.setValue(0)

        # Layout form
        controls_box = QGroupBox("ปรับแต่งภาพ")
        form = QFormLayout()
        form.addRow("Brightness", self.slider_brightness)
        form.addRow("Contrast", self.slider_contrast)
        form.addRow("Saturation", self.slider_saturation)
        form.addRow("Hue", self.slider_hue)
        controls_box.setLayout(form)

        # Layout หลัก
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_preview, stretch=1)
        layout.addWidget(controls_box)
        self.setLayout(layout)

        # Timer update frame
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # ~30 fps

    @Slot()
    def update_frame(self):
        frame = self.picam2.capture_array()
        if frame is None:
            return

        # ------------------------
        # ปรับค่าภาพ
        # ------------------------

        # Brightness & Contrast
        brightness = self.slider_brightness.value()
        contrast = self.slider_contrast.value()

        # alpha: contrast factor, beta: brightness
        alpha = 1 + (contrast / 100.0)  # scale
        beta = brightness               # shift
        adjusted = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

        # Hue & Saturation (ต้องทำใน HSV)
        hsv = cv2.cvtColor(adjusted, cv2.COLOR_BGR2HSV).astype(np.int16)
        hue_shift = self.slider_hue.value()
        sat_scale = self.slider_saturation.value() / 100.0

        # ปรับ Hue
        hsv[..., 0] = (hsv[..., 0] + hue_shift) % 180
        # ปรับ Saturation
        hsv[..., 1] = np.clip(hsv[..., 1] * sat_scale, 0, 255)

        adjusted = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

        # ------------------------
        # แสดงผล
        # ------------------------
        pix = cvimg_to_qpixmap(adjusted)
        self.lbl_preview.setPixmap(pix.scaled(
            self.lbl_preview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))

    def closeEvent(self, event):
        self.picam2.stop()
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CameraApp()
    win.show()
    sys.exit(app.exec())
