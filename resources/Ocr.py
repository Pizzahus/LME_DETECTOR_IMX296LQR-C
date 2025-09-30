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
    def _detect_and_recognize_text(self, image):
        preprocessed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        preprocessed_image = cv2.GaussianBlur(preprocessed_image, (5, 5), 0)
        preprocessed_image = cv2.threshold(preprocessed_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # ใช้ Pytesseract อ่านข้อความ OCR พร้อมตำแหน่ง
        config = (
            r"--oem 1 --psm 6 "
            r"-c tessedit_char_whitelist=0123456789/ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
        data = pytesseract.image_to_data(preprocessed_image, lang="label", config=config, output_type=pytesseract.Output.DICT)


        # วาดกรอบรอบข้อความและกรองผลลัพธ์ในลูปเดียวกัน
        filtered_results = []
        for i in range(len(data["text"])):
            text = data["text"][i]
            confidence = int(data["conf"][i])
            
            # ใช้เงื่อนไขกรองเดียวกันทั้งการวาดกรอบและการเก็บผลลัพธ์
            if confidence > 90 and text.strip():
                filtered_results.append(text)
                
                # วาดกรอบรอบข้อความที่ผ่านการกรอง
                x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                
                # คำนวณความกว้างของแต่ละตัวอักษรโดยประมาณ
                char_width = w / len(text)
                
                # ตีกรอบแต่ละตัวอักษร
                for j, char in enumerate(text):
                    char_x = int(x + j * char_width)
                    char_w = int(char_width)
                    
                    # วาดกรอบรอบตัวอักษร
                    cv2.rectangle(image, (char_x, y), (char_x + char_w, y + h), self.rectColor, 1)
                    
                    # วาดตัวอักษร (optional)
                    cv2.putText(image, char, (char_x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, self.rectColor, 1)

        # รวมข้อความที่กรองแล้วเป็น string เดียว
        recognized_text = " ".join(filtered_results)
        processed_image = image

        return (processed_image, preprocessed_image, recognized_text)

    def run(self):
        while self.running:
            try:
                # รอ frame จากคิว
                frame = self.task_queue.get(timeout=0.1)
            except queue.Empty:
                continue

            start = time.perf_counter()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            processed_image, preprocessed_image, recognized_text = self._detect_and_recognize_text(gray)
            processing_time = time.perf_counter() - start

            self.finished.emit(processed_image, preprocessed_image, recognized_text, processing_time)
            self.task_queue.task_done()

    def stop(self):
        self.running = False
        self.wait()