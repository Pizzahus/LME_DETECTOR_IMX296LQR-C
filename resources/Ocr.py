import queue
import pytesseract
import time
import numpy as np
import cv2
from PySide6.QtCore import QThread, Signal

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

# ===== Worker OCR (Queue-based) =====
class OcrWorker(QThread):
    finished = Signal(np.ndarray, np.ndarray, str, float)  # ถ้า import numpy as np แล้ว

    def __init__(self, task_queue):
        super().__init__()
        self.task_queue = task_queue
        self.rectColor = (255, 17, 0)
        self.running = True

    # ตั้งค่าให้แสดงภาพที่จับได้
    def detect_and_recognize_text(self, image, angle=90):
        """
        image: ภาพ BGR
        angle: หมุนภาพก่อน OCR (องศา, +ve = หมุนตามเข็มนาฬิกา)
        """
        start = time.perf_counter()

        # หมุนภาพถ้ามีการระบุ angle
        if angle != 0:
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            image = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

        # แปลงเป็น grayscale และทำ preprocessing
        preprocessed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        preprocessed_image = cv2.GaussianBlur(preprocessed_image, (5, 5), 0)
        preprocessed_image = cv2.threshold(preprocessed_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # ใช้ Pytesseract อ่านข้อความ OCR พร้อมตำแหน่ง
        config = (
            r"--oem 1 --psm 6 "
            r"-c tessedit_char_whitelist=0123456789/ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
        data = pytesseract.image_to_data(preprocessed_image, lang="label", output_type=pytesseract.Output.DICT)

        # วาดกรอบรอบข้อความและกรองผลลัพธ์
        filtered_results = []
        for i in range(len(data["text"])):
            text = data["text"][i]
            confidence = int(data["conf"][i])
            if confidence > 30 and text.strip():
                filtered_results.append(text)
                x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                char_width = w / len(text)
                for j, char in enumerate(text):
                    char_x = int(x + j * char_width)
                    char_w = int(char_width)
                    cv2.rectangle(preprocessed_image, (char_x, y), (char_x + char_w, y + h), self.rectColor, 1)
                    cv2.putText(preprocessed_image, char, (char_x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, self.rectColor, 1)

        recognized_text = " ".join(filtered_results)
        processed_image = image
        processing_time = time.perf_counter() - start

        return (processed_image, preprocessed_image, recognized_text, processing_time)

    def run(self):
        while self.running:
            try:
                frame = self.task_queue.get(timeout=0.1)
            except queue.Empty:
                continue

            processed_image, preprocessed_image, recognized_text, processing_time = self.detect_and_recognize_text(frame)
            self.finished.emit(processed_image, preprocessed_image, recognized_text, processing_time)
            self.task_queue.task_done()

    def stop(self):
        self.running = False
        self.wait()