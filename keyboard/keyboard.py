# pip install PySide6-Addons

import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PySide6.QtCore import Qt

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
os.environ["QT_QPA_PLATFORM"] = "xcb"   # ถ้าใช้ Wayland แล้ว error

class InputTypeDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Type Demo")
        self.resize(400, 200)

        layout = QVBoxLayout(self)

        # ช่องปกติ
        normal = QLineEdit()
        normal.setPlaceholderText("พิมพ์ข้อความได้ตามปกติ")
        layout.addWidget(normal)

        # ตัวเลขเท่านั้น
        number = QLineEdit()
        number.setPlaceholderText("กรอกเฉพาะตัวเลข")
        number.setInputMethodHints(Qt.ImhDigitsOnly)
        layout.addWidget(number)

        # email
        email = QLineEdit()
        email.setPlaceholderText("กรอกอีเมล")
        email.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        layout.addWidget(email)

        # วันที่
        date = QLineEdit()
        date.setPlaceholderText("กรอกวันที่")
        date.setInputMethodHints(Qt.ImhDate)
        layout.addWidget(date)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputTypeDemo()
    window.show()
    sys.exit(app.exec())
