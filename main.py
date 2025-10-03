import sys
import os
from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QApplication
from PySide6.QtQuickWidgets import QQuickWidget
from ui import LMEDetect

##################################### ตั้งค่า ######################################
OS_NAME = "Linux"  # ตั้งค่าระบบปฏิบัติการ
SCREEN_NUMBER = 0  # หน้าจอ
qml_path = os.path.join(os.path.dirname(__file__), "keyboard.qml")


def main():
    app = QApplication(sys.argv)

    screens = app.screens()
    second_screen = screens[SCREEN_NUMBER]

    # ===== สร้างหน้าต่างหลัก =====
    window = LMEDetect(OS_NAME)
    window.resize(1024, 600)
    window.move(0, 0)
    window.setWindowTitle("ระบบตรวจสอบการพิมพ์")
    window.setWindowFlags(
        Qt.FramelessWindowHint | Qt.WindowTitleHint | Qt.WindowStaysOnTopHint
    )
    window.setGeometry(second_screen.availableGeometry())
    window.showFullScreen()

    # # ===== โหลด QML overlay =====
    # qml_overlay = QQuickWidget(window)
    # qml_overlay.setSource(QUrl.fromLocalFile(qml_path))
    # qml_overlay.setResizeMode(QQuickWidget.SizeRootObjectToView)
    # qml_overlay.setClearColor(Qt.transparent)
    # qml_overlay.setAttribute(Qt.WA_TranslucentBackground)
    # qml_overlay.setAttribute(Qt.WA_AlwaysStackOnTop)
    # qml_overlay.setGeometry(0, 0, 1024, 600)
    # qml_overlay.hide() # ซ่อน keyboard ตอนเริ่มต้น
    # root_obj = qml_overlay.rootObject()

    # # ===== สมมติ LMEDetect มี QLineEdit =====
    # input_fields = []
    # if hasattr(window, "lineEdit"):
    #     input_fields.append(window.lineEdit)

    # # hook event focus
    # for field in input_fields:
    #     old_focus_in = field.focusInEvent
    #     old_focus_out = field.focusOutEvent

    #     def focus_in(event, f=field):
    #         qml_overlay.show()
    #         if root_obj and hasattr(root_obj, "setActiveField"):
    #             root_obj.setActiveField(f)
    #             print(field)
    #         if old_focus_in:
    #             old_focus_in(event)

    #     def focus_out(event, f=field):
    #         print(field)
    #         qml_overlay.hide()
    #         if old_focus_out:
    #             old_focus_out(event)

    #     field.focusInEvent = focus_in
    #     field.focusOutEvent = focus_out

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
