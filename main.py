import sys
import os
from PySide6.QtCore import Qt, QUrl, QTimer
from PySide6.QtWidgets import QApplication
from PySide6.QtQuickWidgets import QQuickWidget
from ui import LMEDetect

##################################### ตั้งค่า ######################################
SCREEN_NUMBER = 0

#  Keyboard
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
os.environ["QT_QPA_PLATFORM"] = "xcb"
qml_path = os.path.join(os.path.dirname(__file__), "keyboard.qml")


def main():
    app = QApplication(sys.argv)

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


    # ===== Keyboard =====
    qml_overlay = QQuickWidget(window)
    qml_overlay.setSource(QUrl.fromLocalFile(qml_path))
    qml_overlay.setResizeMode(QQuickWidget.SizeRootObjectToView)
    qml_overlay.setClearColor(Qt.transparent)
    qml_overlay.setAttribute(Qt.WA_TranslucentBackground)
    qml_overlay.setAttribute(Qt.WA_AlwaysStackOnTop)
    qml_overlay.setGeometry(0, 0, 1024, 600)
    qml_overlay.hide()
    root_obj = qml_overlay.rootObject()

    input_fields = [
        window.exposureTime,
        window.delayShutter,
        window.lot_set,
        window.mfg_set,
        window.exp_set,
    ]

    # ฟังก์ชันซ่อนคีย์บอร์ด (ใช้ร่วมกันทุกกรณี)
    def hideKeyboard():
        qml_overlay.hide()
        window.activateWindow()
        window.setFocus(Qt.OtherFocusReason)

    # เชื่อม signal จาก QML
    if root_obj and hasattr(root_obj, "reqHideKeyboard"):
        root_obj.reqHideKeyboard.connect(hideKeyboard)

    # Hook focus events
    for field in input_fields:
        old_focus_in = field.focusInEvent
        old_focus_out = field.focusOutEvent

        def make_handlers(field):
            def focus_in(event):
                qml_overlay.show()
                if root_obj and hasattr(root_obj, "setActiveField"):
                    root_obj.setActiveField(field)
                if old_focus_in:
                    old_focus_in(event)

            def focus_out(event):
                if (root_obj and 
                    hasattr(root_obj, 'activeField') and 
                    root_obj.property('activeField') == field):
                    hideKeyboard()
                if old_focus_out:
                    old_focus_out(event)

            return focus_in, focus_out


        focus_in, focus_out = make_handlers(field)
        field.focusInEvent = focus_in
        field.focusOutEvent = focus_out

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
