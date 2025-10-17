import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt

# เปิด Virtual Keyboard
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
os.environ["QT_QPA_PLATFORM"] = "xcb"   # ถ้าใช้ Wayland แล้ว error
os.environ["QT_VIRTUALKEYBOARD_HIDE_ON_ESCAPE"] = "1"   # ดัน UI ขึ้น ไม่บัง QLineEdit
os.environ["QT_VIRTUALKEYBOARD_PREVIEW"] = "0"   # แสดง preview บน keyboard

class KeyboardOverlayDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keyboard Overlay Fix")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        # Label แสดงข้อความ
        self.display_label = QLabel("ข้อความที่กำลังพิมพ์จะแสดงตรงนี้")
        self.display_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.display_label)

        # QLineEdit สำหรับพิมพ์ (ถึงแม้จะถูกบัง แต่ยังรับ input ได้)
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("แตะเพื่อพิมพ์...")
        layout.addWidget(self.line_edit)

        # sync ข้อความแบบ real-time
        self.line_edit.textChanged.connect(self.update_label)

    def update_label(self, text):
        if text:
            self.display_label.setText(f"คุณพิมพ์: {text}")
        else:
            self.display_label.setText("ข้อความที่กำลังพิมพ์จะแสดงตรงนี้")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyboardOverlayDemo()
    window.show()
    sys.exit(app.exec())
