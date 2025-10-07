from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, QPoint
import sys

class TouchScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._last_pos = None

    def mousePressEvent(self, event):
        self._last_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self._last_pos:
            dx = event.pos().x() - self._last_pos.x()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - dx)
            self._last_pos = event.pos()

    def mouseReleaseEvent(self, event):
        self._last_pos = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Scroll with Drag")

        scroll_area = TouchScrollArea()
        content = QWidget()
        layout = QHBoxLayout(content)

        # เพิ่มปุ่มหลายตัวเรียงแนวนอน
        for i in range(20):
            btn = QPushButton(f"Item {i+1}")
            btn.setFixedSize(120, 80)
            layout.addWidget(btn)

        scroll_area.setWidget(content)
        self.setCentralWidget(scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 200)
    window.show()
    sys.exit(app.exec())