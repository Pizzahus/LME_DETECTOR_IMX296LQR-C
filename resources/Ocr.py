import queue
import pytesseract
import time
import numpy as np
import cv2
from PySide6.QtCore import QThread, Signal
from resources.FramePreprocessor import FramePreprocessor

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

# ===== Worker OCR (Queue-based) =====
class OcrWorker(QThread):
    finished = Signal(np.ndarray, np.ndarray, np.ndarray, str, float)  # ถ้า import numpy as np แล้ว

    def __init__(self, task_queue, angle=0, confidence=0):
        super().__init__()
        self.task_queue = task_queue
        self.rectColor = (255, 17, 0)
        self.running = True
        self.angle=angle
        self.confidence=confidence
        self.preprocessor = FramePreprocessor()

    
    def rotate_image_cover(self, image, angle):
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)

        # สร้าง matrix สำหรับการหมุน
        M = cv2.getRotationMatrix2D(center, angle, 1.0)

        # คำนวณขนาดใหม่ของ canvas
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        new_w = int((h * sin) + (w * cos))
        new_h = int((h * cos) + (w * sin))

        # ปรับ matrix เพื่อให้ภาพอยู่ตรงกลาง canvas ใหม่
        M[0, 2] += (new_w / 2) - center[0]
        M[1, 2] += (new_h / 2) - center[1]

        # หมุนภาพโดยใช้ canvas ใหม่
        rotated = cv2.warpAffine(image, M, (new_w, new_h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        return rotated
    
    # ตั้งค่าให้แสดงภาพที่จับได้
    def detect_and_recognize_text(self, image):
        """
        image: ภาพ BGR
        angle: หมุนภาพก่อน OCR (องศา, +ve = หมุนตามเข็มนาฬิกา)
        """
        start = time.perf_counter()

        original_image = image.copy()  # เก็บภาพต้นฉบับไว้ก่อนแก้ไข

        # หมุนภาพถ้ามีการระบุ angle
        if self.angle != 0:
            image = self.rotate_image_cover(image, self.angle)

        # แปลงเป็น grayscale และทำ preprocessing
        preprocessed_image = self.preprocessor.process(image)

        # ใช้ Pytesseract อ่านข้อความ OCR พร้อมตำแหน่ง
        config = (
            r"--oem 1 --psm 6 "
            r"-c tessedit_char_whitelist=0123456789/ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
        data = pytesseract.image_to_data(preprocessed_image, lang="eng_best", output_type=pytesseract.Output.DICT)

        # วาดกรอบรอบข้อความและกรองผลลัพธ์
        filtered_results = []
        for i in range(len(data["text"])):
            text = data["text"][i]
            confidence = int(data["conf"][i])
            if confidence > self.confidence and text.strip():
                filtered_results.append(text)
                x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                char_width = w / len(text)
                for j, char in enumerate(text):
                    char_x = int(x + j * char_width)
                    char_w = int(char_width)
                    cv2.rectangle(image, (char_x, y), (char_x + char_w, y + h), self.rectColor, 1)
                    cv2.putText(image, char, (char_x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, self.rectColor, 1)

        recognized_text = " ".join(filtered_results)
        processed_image = image
        processing_time = time.perf_counter() - start

        # แปลงเวลาเป็น ms
        processing_ms = processing_time * 1000
        time_text = f"Processing Time: {processing_ms:.1f}ms"

        # ขนาดภาพ
        img_height, img_width = processed_image.shape[:2]

        # ปรับขนาดฟอนต์ตามความสูงของภาพ
        font_scale = img_height / 350.0
        thickness = max(1, int(img_height / 100))

        # คำนวณขนาดข้อความ
        (text_width, text_height), _ = cv2.getTextSize(time_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)

        # ตำแหน่งกึ่งกลางด้านล่าง
        text_x = (img_width - text_width) // 2
        text_y = img_height - 15

        # 🧠 วิเคราะห์สีพื้นหลังใต้ข้อความ
        roi_y1 = max(0, text_y - text_height)
        roi_y2 = min(img_height, text_y + 5)
        roi_x1 = max(0, text_x)
        roi_x2 = min(img_width, text_x + text_width)
        roi = processed_image[roi_y1:roi_y2, roi_x1:roi_x2]

        # คำนวณความสว่างเฉลี่ย
        brightness = int(np.mean(roi)) if roi.size > 0 else 128

        # เลือกสีข้อความให้ตัดกัน
        text_color = (0, 0, 0) if brightness > 128 else (255, 255, 255)

        # วาดข้อความ
        cv2.putText(processed_image, time_text, (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, thickness)



        return (original_image, processed_image, preprocessed_image, recognized_text, processing_time)

    def run(self):
        while self.running:
            try:
                frame = self.task_queue.get(timeout=0.1)
            except queue.Empty:
                continue

            original_image, processed_image, preprocessed_image, recognized_text, processing_time = self.detect_and_recognize_text(frame)
            self.finished.emit(original_image, processed_image, preprocessed_image, recognized_text, processing_time)
            self.task_queue.task_done()

    def stop(self):
        self.running = False
        self.wait()