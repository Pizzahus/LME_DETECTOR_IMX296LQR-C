import time
import cv2
import pytesseract
from PySide6.QtCore import QThread
from multiprocessing import Process, Queue


# ===== ตั้งค่า Tesseract =====
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
IMG_PATH = "test.png"   # เปลี่ยนเป็นภาพที่คุณต้องการ
img = cv2.imread(IMG_PATH)


# ===== Direct Call =====
def test_direct():
    start = time.perf_counter()
    pytesseract.image_to_data(
        img, lang="eng", output_type=pytesseract.Output.DICT
    )
    return time.perf_counter() - start


# ===== QThread =====
class OcrThread(QThread):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.elapsed = None

    def run(self):
        start = time.perf_counter()
        pytesseract.image_to_data(
            self.image, lang="eng", output_type=pytesseract.Output.DICT
        )
        self.elapsed = time.perf_counter() - start


def test_qthread():
    worker = OcrThread(img)
    worker.start()
    worker.wait()
    return worker.elapsed


# ===== Multiprocessing =====
def ocr_process(image, q):
    start = time.perf_counter()
    pytesseract.image_to_data(
        image, lang="eng", output_type=pytesseract.Output.DICT
    )
    elapsed = time.perf_counter() - start
    q.put(elapsed)


def test_multiprocessing():
    q = Queue()
    p = Process(target=ocr_process, args=(img, q))
    p.start()
    p.join()
    return q.get()


# ===== Main Benchmark =====
if __name__ == "__main__":
    print("=== Direct ===")
    print("Direct:", test_direct())

    print("=== QThread ===")
    print("QThread:", test_qthread())

    print("=== Multiprocessing ===")
    print("Multiprocessing:", test_multiprocessing())
