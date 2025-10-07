import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from ui import LMEDetect

##################################### ตั้งค่า ######################################
SCREEN_NUMBER = 0

# #  Keyboard
# os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
# os.environ["QT_QPA_PLATFORM"] = "xcb"
# qml_path = os.path.join(os.path.dirname(__file__), "keyboard.qml")

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    screens = app.screens()
    if not screens:
        print("ไม่พบหน้าจอ!")
        sys.exit(1)
    second_screen = screens[SCREEN_NUMBER]

    window = LMEDetect()
    window.resize(1024, 600)
    window.setWindowTitle("ระบบตรวจสอบการพิมพ์")
    window.setWindowFlags(
        Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
    )
    window.setGeometry(second_screen.availableGeometry())
    window.showFullScreen()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
