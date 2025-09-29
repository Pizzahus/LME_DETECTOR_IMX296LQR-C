import queue
import pytesseract
from PySide6.QtCore import QTimer, QThread, Signal, Qt

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