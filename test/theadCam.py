import sys
import cv2
import pytesseract
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit, QSizePolicy
)
from PySide6.QtCore import QTimer, QThread, Signal, Qt
from PySide6.QtGui import QImage, QPixmap
from picamera2 import Picamera2


# ===== Worker Thread OCR =====
class OcrWorker(QThread):
    finished = Signal(str)

    def __init__(self, frame):
        super().__init__()
        self.frame = frame

    def run(self):
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray, lang="label")  # ปรับ lang ได้
        self.finished.emit(text)




# ===== Main GUI =====
class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OCR Camera (PySide6 + Picamera2)")
        self.resize(1000, 700)

        # UI Components
        self.label = QLabel("Camera preview")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)  # ทำให้ภาพย่อ/ขยายตาม QLabel
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btn_capture = QPushButton("📸 ถ่ายภาพ + OCR")
        self.text_output = QTextEdit()
        self.text_output.setPlaceholderText("ผลลัพธ์ OCR จะแสดงที่นี่...")
        self.text_output.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(self.label, stretch=3)
        layout.addWidget(self.btn_capture, stretch=0)
        layout.addWidget(self.text_output, stretch=1)
        self.setLayout(layout)

        # Camera setup
        self.picam2 = Picamera2()
        self.picam2.preview_configuration.main.size = (640, 480)
        self.picam2.preview_configuration.main.format = "RGB888"
        self.picam2.configure("preview")
        self.picam2.start()

        # Timer อัปเดตภาพ preview
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # ~30 FPS

        # Button action
        self.btn_capture.clicked.connect(self.capture_image)

        # เก็บ threads ป้องกันถูกเก็บทิ้ง
        self.threads = []

        # buffer ล่าสุดไว้ย่อขนาด
        self.current_frame = None

    def update_frame(self):
        frame = self.picam2.capture_array()
        self.current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.show_frame()

    def show_frame(self):
        if self.current_frame is not None:
            h, w, ch = self.current_frame.shape
            qimg = QImage(self.current_frame.data, w, h, ch * w, QImage.Format_RGB888)
            pix = QPixmap.fromImage(qimg)
            # ปรับให้พอดีกับ QLabel
            self.label.setPixmap(pix.scaled(
                self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.show_frame()  # อัปเดตภาพใหม่เวลาหน้าต่างถูกย่อ/ขยาย

    def capture_image(self):
        if self.current_frame is None:
            return
        frame_bgr = cv2.cvtColor(self.current_frame, cv2.COLOR_RGB2BGR)

        # สร้าง OCR Thread
        worker = OcrWorker(frame_bgr)
        worker.finished.connect(self.show_ocr_result)
        worker.start()
        self.threads.append(worker)  # เก็บอ้างอิงไว้ไม่ให้ถูกลบทิ้ง

    def show_ocr_result(self, text):
        self.text_output.append("==== OCR Result ====\n" + text.strip() + "\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CameraApp()
    win.show()
    sys.exit(app.exec())
