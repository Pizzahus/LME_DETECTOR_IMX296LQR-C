import sys
import os
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
os.environ["QT_QPA_PLATFORM"] = "xcb"   # ถ้าใช้ Wayland แล้ว error
qml_path = os.path.join(os.path.dirname(__file__), "main.qml")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Qt Virtual Keyboard + Overlay TextField")
window.resize(600, 400)

layout = QVBoxLayout(window)

qml_widget = QQuickWidget()
qml_widget.setResizeMode(QQuickWidget.SizeRootObjectToView)
qml_widget.setSource(QUrl.fromLocalFile(qml_path))

layout.addWidget(qml_widget)
window.show()

sys.exit(app.exec())
