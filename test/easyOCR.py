import sys
import os
import time
import cv2
import numpy as np
import easyocr

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt

reader = easyocr.Reader(['en'], gpu=False)

class OCRViewer(QWidget):
    def __init__(self, image_paths):
        super().__init__()
        self.image_paths = image_paths
        self.index = 0

        self.setWindowTitle("OCR Viewer")
        self.image_label = QLabel()
        self.time_label = QLabel()
        self.next_button = QPushButton("ถัดไป ▶️")

        self.next_button.clicked.connect(self.show_next_image)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.time_label)
        layout.addWidget(self.next_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

        self.show_next_image()
    
    def resize_image(self, image, scale_percent=50):
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized

    def show_next_image(self):
        if self.index >= len(self.image_paths):
            self.image_label.setText("✅ ดูครบทุกภาพแล้ว")
            self.time_label.setText("")
            self.next_button.setEnabled(False)
            return

        image_path = self.image_paths[self.index]
        image = cv2.imread(image_path)
        image = self.resize_image(image, 50)

        start_time = time.time()
        result = reader.readtext(image)
        elapsed_time = time.time() - start_time

        print(result)

        for bbox, text, confidence in result:
            pts = [tuple(map(int, point)) for point in bbox]
            cv2.polylines(image, [np.array(pts)], isClosed=True, color=(0, 255, 0), thickness=2)
            x, y = pts[0]
            cv2.putText(image, f'{text} ({confidence:.2f})', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(q_image)

        self.image_label.setPixmap(pixmap)
        self.time_label.setText(f"🕒 ใช้เวลา: {elapsed_time:.2f} วินาที\n📄 ไฟล์: {os.path.basename(image_path)}")
        self.resize(pixmap.width(), pixmap.height() + 80)

        self.index += 1

def run_batch_viewer(folder_path="./OCR"):
    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
    image_paths.sort()

    app = QApplication(sys.argv)
    viewer = OCRViewer(image_paths)
    viewer.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_batch_viewer()