import sys
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from ui import LMEDetect

##################################### ตั้งค่า ######################################
OS_NAME = "Linux"  # ตั้งค่าระบบปฏิบัติการ
SCREEN_NUMBER = 0  # หน้าจอ

# if OS_NAME == "Windows":
#     os.environ["QT_MEDIA_BACKEND"] = "windows"
# elif OS_NAME == "Linux":
#     os.environ["QT_MEDIA_BACKEND"] = "gstreamer"


def main():
    app = QApplication(sys.argv)

    # เลือกจอที่สอง
    screens = app.screens()
    second_screen = screens[SCREEN_NUMBER]

    # สร้างหน้าต่างหลัก
    window = LMEDetect(OS_NAME)
    window.resize(1024, 600)
    # window.resize(1280, 800)
    window.move(0, 0)
    window.setWindowTitle("ระบบตรวจสอบการพิมพ์")
    # window.setWindowFlags(
    #     Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowStaysOnTopHint
    # )
    # window.setGeometry(second_screen.availableGeometry())  # ให้หน้าต่างเต็มจอ
    # window.showFullScreen()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
