import queue
import time
import numpy as np
import easyocr
import pytesseract
import cv2
from PySide6.QtCore import QThread, Signal
from resources.FramePreprocessor import FramePreprocessor

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

# ===== Worker OCR (Queue-based) =====
class OcrWorker(QThread):
    finished = Signal(np.ndarray, np.ndarray, np.ndarray, str, float)

    def __init__(self, task_queue, angle=0, confidence=0, engine="tesseract", resize_percent=50):
            super().__init__()
            self.task_queue = task_queue
            self.rectColor = (255, 17, 0)
            self.running = True
            self.angle = angle
            self.confidence = confidence
            self.preprocessor = FramePreprocessor()
            self.engine = engine
            self.pytesseract = pytesseract
            self.set_engine(engine)
            self.reader = easyocr.Reader(['en'], gpu=False)
            self.resize_percent = resize_percent
            self.tesseract_model = 'eng'

    def resize_image(self, image, scale_percent=50):
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized

    def set_tesseract_model(self, model_name):
        if model_name == self.tesseract_model:
            return  # ไม่ต้องเปลี่ยนถ้าเหมือนเดิม
        self.tesseract_model = model_name

    # เลือก Engine ในการอ่านข้อความ
    def set_engine(self, engine_name):
        engine_name = engine_name.lower()
        if engine_name == self.engine:
            return  # ไม่ต้องเปลี่ยนถ้าเหมือนเดิม
        self.engine = engine_name

    def rotate_image_cover(self, image, angle):
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        new_w = int((h * sin) + (w * cos))
        new_h = int((h * cos) + (w * sin))
        M[0, 2] += (new_w / 2) - center[0]
        M[1, 2] += (new_h / 2) - center[1]
        rotated = cv2.warpAffine(image, M, (new_w, new_h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        return rotated

    def detect_and_recognize_text(self, image):
        start = time.perf_counter()
        original_image = image.copy()

        if self.angle != 0:
            image = self.rotate_image_cover(image, self.angle)

        image = self.resize_image(image=image, scale_percent=self.resize_percent)
        preprocessed_image = self.preprocessor.process(image)
        filtered_results = []

        if self.engine == "easyocr":
            results = self.reader.readtext(preprocessed_image)
            for bbox, text, conf in results:
                if conf * 100 > self.confidence and text.strip():
                    filtered_results.append(text)
                    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = bbox
                    x, y, w, h = int(x0), int(y0), int(x2 - x0), int(y2 - y0)
                    char_width = w / max(len(text), 1)
                    for j, char in enumerate(text):
                        char_x = int(x + j * char_width)
                        char_w = int(char_width)
                        cv2.rectangle(image, (char_x, y), (char_x + char_w, y + h), self.rectColor, 1)

                        if self.resize_percent >= 80:
                            cv2.putText(image, char, (char_x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, self.rectColor, 1)

        elif self.engine == "tesseract":
            config = (
                r"--oem 1 --psm 6 "
                r"-c tessedit_char_whitelist=0123456789/ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            )
            data = self.pytesseract.image_to_data(preprocessed_image, lang=self.tesseract_model, config=config, output_type=self.pytesseract.Output.DICT)
            for i in range(len(data["text"])):
                text = data["text"][i]
                confidence = int(data["conf"][i])
                if confidence > self.confidence and text.strip():
                    filtered_results.append(text)
                    x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                    char_width = w / max(len(text), 1)
                    for j, char in enumerate(text):
                        char_x = int(x + j * char_width)
                        char_w = int(char_width)
                        cv2.rectangle(image, (char_x, y), (char_x + char_w, y + h), self.rectColor, 1)

                        if self.resize_percent >= 80:
                            cv2.putText(image, char, (char_x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, self.rectColor, 1)

        recognized_text = " ".join(filtered_results)
        processed_image = image
        processing_time = time.perf_counter() - start
        processing_ms = processing_time * 1000
        time_text = f"Processing Time: {processing_ms:.1f}ms"

        img_height, img_width = processed_image.shape[:2]
        font_scale = img_height / 350.0
        thickness = max(1, int(img_height / 100))
        (text_width, text_height), _ = cv2.getTextSize(time_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
        text_x = (img_width - text_width) // 2
        text_y = img_height - 15

        roi_y1 = max(0, text_y - text_height)
        roi_y2 = min(img_height, text_y + 5)
        roi_x1 = max(0, text_x)
        roi_x2 = min(img_width, text_x + text_width)
        roi = processed_image[roi_y1:roi_y2, roi_x1:roi_x2]
        brightness = int(np.mean(roi)) if roi.size > 0 else 128
        text_color = (0, 0, 0) if brightness > 128 else (255, 255, 255)

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