import time
import queue
from gpiozero import Button, OutputDevice
from PySide6.QtCore import QThread, Signal


class Item:
    """งานแต่ละชิ้น"""
    def __init__(self, tag: str, status: str):
        self.tag = tag
        self.status = status.upper()  # "OK" หรือ "NG"


class RejectionWorker(QThread):
    """
    Worker สำหรับจัดการกระบวนการ Reject โดยใช้ Sensor + Queue

    การทำงาน:
    - ทุกครั้งที่ sensor ถูก trigger → จะดึงงาน 1 ชิ้นจาก queue
    - งานใน queue จะถูกระบุว่าเป็น "OK" หรือ "NG"
    - ถ้าเป็น OK → ไม่ทำอะไร แค่ผ่านไป
    - ถ้าเป็น NG → จะรอเวลา (rejectDelay วินาที) แล้วสั่ง rejectPin ทำงาน (เช่น เปิดโซลินอยด์/รีเลย์)
    - รองรับ startReject: สร้างงาน reject ล่วงหน้า N ชิ้นตั้งแต่เริ่มต้น
    - ใช้ในระบบแบบ 1 trigger : 1 งาน (ไม่ข้ามคิว ไม่ซ้อนคิว)
    """
    rejected_signal = Signal(str)  # ส่ง tag ของงานที่ reject ไป GUI

    def __init__(self, sensor: Button, rejector: OutputDevice, startReject: int=0, rejectDelay: int=100, rejectionPeriod: int=100):
        super().__init__()
        self.running = True
        self.rejectDelay = rejectDelay  # เวลาหน่วงก่อน reject
        self.rejectionPeriod = rejectionPeriod  # ระยะเวลา reject

        # Queue งาน
        self.task_queue = queue.Queue()

        # ถ้า startReject > 0 ให้สร้าง queue ล่วงหน้า
        for i in range(1, startReject + 1):
            self.put_task(f"start reject {i}", "NG")

        # Sensor
        self.sensor = sensor
        self.sensor.when_pressed = self._sensor_triggered

        # Reject pin
        self.rejector = rejector

    def put_task(self, tag: str, status: str):
        """เพิ่มงาน OK/NG เข้า queue"""
        item = Item(tag, status)
        self.task_queue.put(item)

    def _sensor_triggered(self):
        """เมื่อ sensor detect → จับงาน 1 ชิ้นจาก queue"""
        if self.task_queue.empty():
            # print("⚠️ ไม่มีงานใน queue แต่ sensor triggered")
            return

        item = self.task_queue.get()
        print(f"Sensor triggered → {item.tag} [{item.status}]")

        if item.status == "NG":
            print(f"NG detected: {item.tag} → wait {self.rejectDelay}ms before reject")
            time.sleep(self.rejectDelay * 0.001)
            self._reject(item)

        self.task_queue.task_done()

    def _reject(self, item: Item):
        """สั่ง reject pin สำหรับงาน NG"""
        print(f">>> REJECT: {item.tag}")
        self.rejector.on()
        time.sleep(self.rejectionPeriod * 0.001)  # ระยะเวลาเปิด reject
        self.rejector.off()
        self.rejected_signal.emit(item.tag)

    def run(self):
        while self.running:
            time.sleep(0.05)  # idle loop, sensor trigger ทำงานผ่าน callback

    def stop(self):
        self.running = False
        self.wait()