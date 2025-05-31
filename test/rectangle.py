from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtGui import QPainter, QPen, QColor, QMouseEvent
from PySide6.QtCore import Qt, QRect, QPoint, Signal
import sys


class WebcamMonitor(QWidget):
    # Signal คืนค่าพิกัด rectangle
    rect_drawn = Signal(int, int, int, int)

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.drawing = False
        self.rect = QRect()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.start_point = event.position().toPoint()
            self.end_point = event.position().toPoint()
            self.drawing = True
            self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.drawing:
            self.end_point = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.end_point = event.position().toPoint()
            self.drawing = False
            self.rect = QRect(self.start_point, self.end_point).normalized()
            self.update()

            # ส่งสัญญาณพร้อมพิกัด x1, y1, x2, y2
            self.rect_drawn.emit(self.rect.left(), self.rect.top(), self.rect.right(), self.rect.bottom())

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.drawing or not self.rect.isNull():
            painter = QPainter(self)
            pen = QPen(QColor(0, 255, 0), 2, Qt.SolidLine)
            painter.setPen(pen)
            rect = QRect(self.start_point, self.end_point).normalized()
            painter.drawRect(rect)


# ทดสอบ signal
def handle_rect(x1, y1, x2, y2):
    print(f"กรอบถูกลากที่: x1={x1}, y1={y1}, x2={x2}, y2={y2}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QWidget()
    layout = QVBoxLayout(main_window)

    webcam_monitor = WebcamMonitor()
    webcam_monitor.setStyleSheet("background-color: black;")
    webcam_monitor.rect_drawn.connect(handle_rect)  # เชื่อมต่อ signal

    layout.addWidget(webcam_monitor)

    main_window.resize(640, 480)
    main_window.show()
    sys.exit(app.exec())
