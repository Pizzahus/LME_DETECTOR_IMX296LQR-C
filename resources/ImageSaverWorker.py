from datetime import datetime
import os
import cv2
import queue
from PySide6.QtCore import QThread

class ImageSaverWorker(QThread):
    """Worker สำหรับบันทึกภาพลงโฟลเดอร์ OK/NG + prefix แบบไม่ขัด UI"""
    def __init__(self, save_dir="captured_images", parent=None):
        super().__init__(parent)
        self.save_dir = save_dir
        self.task_queue = queue.Queue()
        self.running = True

    def put(self, image, status: bool, prefix="capture"):
        """เพิ่มงานลง queue เพื่อบันทึกภาพ"""
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S") + f"_{now.microsecond:06d}"
        filename = f"{timestamp}.png"

        status_folder = "ok" if status else "ng"
        target_dir = os.path.join(self.save_dir, status_folder, prefix)
        os.makedirs(target_dir, exist_ok=True)

        full_path = os.path.join(target_dir, filename)
        self.task_queue.put((image, full_path))

    def run(self):
        while self.running:
            try:
                image, path = self.task_queue.get(timeout=0.1)
                cv2.imwrite(path, image)
                self.task_queue.task_done()
            except queue.Empty:
                continue

    def stop(self):
        self.running = False
        self.wait()