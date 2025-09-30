import cv2
import pytesseract
import time
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from PySide6.QtCore import QObject, Signal, QCoreApplication

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

# ========== OCR Handler (ใช้ Executor) ==========
class OcrWorker(QObject):
    finished = Signal(np.ndarray, np.ndarray, str, float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.rectColor = (255, 17, 0)
        # สร้าง ThreadPoolExecutor ขนาด 1 worker
        self.executor = ThreadPoolExecutor(max_workers=1)

    def run_ocr(self, frame: np.ndarray):
        """ส่งงานไปให้ executor ทำ OCR"""
        future = self.executor.submit(self._detect_and_recognize_text, frame)
        future.add_done_callback(self._on_done)

    def _detect_and_recognize_text(self, image: np.ndarray):
        start = time.perf_counter()

        # ----- Preprocess -----
        preprocessed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        preprocessed_image = cv2.GaussianBlur(preprocessed_image, (5, 5), 0)
        preprocessed_image = cv2.threshold(
            preprocessed_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
        )[1]

        # ----- OCR -----
        config = (
            r"--oem 1 --psm 6 "
            r"-c tessedit_char_whitelist=0123456789/ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
        data = pytesseract.image_to_data(
            preprocessed_image, 
            lang="label",
            output_type=pytesseract.Output.DICT
        )

        # ----- Postprocess -----
        filtered_results = []
        for i in range(len(data["text"])):
            text = data["text"][i]
            conf_str = data["conf"][i]
            try:
                confidence = int(conf_str)
            except ValueError:
                confidence = -1

            if text.strip() and confidence > 0:
                filtered_results.append(text)

                x, y, w, h = (
                    data["left"][i],
                    data["top"][i],
                    data["width"][i],
                    data["height"][i],
                )
                if len(text) > 0:
                    char_width = w / len(text)
                    for j, char in enumerate(text):
                        char_x = int(x + j * char_width)
                        char_w = int(char_width)
                        cv2.rectangle(
                            image,
                            (char_x, y),
                            (char_x + char_w, y + h),
                            self.rectColor,
                            1,
                        )
                        cv2.putText(
                            image,
                            char,
                            (char_x, y - 5),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.4,
                            self.rectColor,
                            1,
                        )

        recognized_text = " ".join(filtered_results)
        processing_time = time.perf_counter() - start
        return image, preprocessed_image, recognized_text, processing_time

    def _on_done(self, future):
        """callback จาก executor เสร็จงาน"""
        try:
            processed_image, preprocessed_image, recognized_text, processing_time = future.result()
            # emit สัญญาณกลับไป main thread (Qt จะจัดการ thread-safe ให้เอง)
            self.finished.emit(processed_image, preprocessed_image, recognized_text, processing_time)
        except Exception as e:
            print("OCR error:", e)

    def shutdown(self):
        self.executor.shutdown(wait=False)
