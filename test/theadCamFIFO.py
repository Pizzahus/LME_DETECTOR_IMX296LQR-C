import sys
import cv2
import pytesseract
import time
import queue
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QTextEdit, QSizePolicy
)
from PySide6.QtCore import QTimer, QThread, Signal, Qt
from PySide6.QtGui import QImage, QPixmap
from picamera2 import Picamera2


# ===== Worker OCR (Queue-based) =====
class OcrWorker(QThread):
    finished = Signal(str, float)  # ส่งผลลัพธ์ + เวลา

    def __init__(self, task_queue):
        super().__init__()
        self.task_queue = task_queue
        self.running = True

    def run(self):
        while self.running:
            try:
                # รอ frame จากคิว
                frame = self.task_queue.get(timeout=0.1)
            except queue.Empty:
                continue

            start = time.perf_counter()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray, lang="label")
            elapsed = time.perf_counter() - start

            self.finished.emit(text, elapsed)
            self.task_queue.task_done()

    def stop(self):
        self.running = False
        self.wait()


# ===== Main GUI =====
class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OCR Camera (Queue + Worker)")
        self.resize(1200, 700)

        # ===== UI Components =====
        self.label = QLabel("Camera preview")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btn_capture = QPushButton("📸 ถ่ายภาพ + OCR")

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.label, stretch=3)
        left_layout.addWidget(self.btn_capture, stretch=0)

        self.text_output = QTextEdit()
        self.text_output.setPlaceholderText("ผลลัพธ์ OCR จะแสดงที่นี่...")
        self.text_output.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, stretch=3)
        main_layout.addWidget(self.text_output, stretch=2)
        self.setLayout(main_layout)

        # ===== Camera setup =====
        self.picam2 = Picamera2()
        self.picam2.preview_configuration.main.size = (640, 480)
        self.picam2.preview_configuration.main.format = "RGB888"
        self.picam2.configure("preview")
        self.picam2.start()

        # Timer อัปเดตภาพ preview
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        # Button action
        self.btn_capture.clicked.connect(self.capture_image)

        # ===== Queue OCR =====
        self.task_queue = queue.Queue()
        self.worker = OcrWorker(self.task_queue)
        self.worker.finished.connect(self.show_ocr_result)
        self.worker.start()

        self.current_frame = None
        self.ocr_count = 0

    def update_frame(self):
        frame = self.picam2.capture_array()
        self.current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.show_frame()

    def show_frame(self):
        if self.current_frame is not None:
            h, w, ch = self.current_frame.shape
            qimg = QImage(self.current_frame.data, w, h, ch * w, QImage.Format_RGB888)
            pix = QPixmap.fromImage(qimg)
            self.label.setPixmap(pix.scaled(
                self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.show_frame()

    def capture_image(self):
        if self.current_frame is None:
            return
        frame_bgr = cv2.cvtColor(self.current_frame, cv2.COLOR_RGB2BGR)
        self.task_queue.put(frame_bgr)  # ใส่งานเข้า Queue

    def show_ocr_result(self, text, elapsed):
        self.ocr_count += 1
        self.text_output.append(
            f"[{self.ocr_count}] ใช้เวลา {elapsed:.2f} วินาที\n{text.strip()}\n"
        )

    def closeEvent(self, event):
        self.worker.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CameraApp()
    win.show()
    sys.exit(app.exec())
