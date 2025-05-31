from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPainter, QPen, QColor, QMouseEvent, QPixmap
from PySide6.QtCore import QEvent, Qt, QRect, QPoint, Signal


class Rectangle(QWidget):
    rect_drawn = Signal(int, int, int, int)

    def __init__(self, label: QLabel):
        super().__init__(label)
        self.label = label
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)  # อนุญาตให้รับเหตุการณ์เมาส์
        self.setGeometry(self.label.rect())  # กำหนดขนาดให้เท่ากับ label
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.drawing = False
        self.rect = QRect()

    def eventFilter(self, obj, event):
        if obj == self.label:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.start_point = event.position().toPoint()
                self.end_point = self.start_point
                self.drawing = True
                self.update()  # อัพเดทเฉพาะวิดเจ็ตนี้
                return True

            elif event.type() == QEvent.MouseMove and self.drawing:
                self.end_point = event.position().toPoint()
                self.update()
                return True

            elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self.end_point = event.position().toPoint()
                self.drawing = False
                self.rect = QRect(self.start_point, self.end_point).normalized()
                self.rect_drawn.emit(self.rect.left(), self.rect.top(), self.rect.right(), self.rect.bottom())
                self.update()
                return True
        return False

    def paintEvent(self, event):
        if self.drawing or not self.rect.isNull():
            painter = QPainter(self)
            pen = QPen(QColor(255, 0, 0), 2, Qt.SolidLine)
            painter.setPen(pen)
            rect = QRect(self.start_point, self.end_point).normalized()
            painter.drawRect(rect)
            
    def resizeEvent(self, event):
        self.setGeometry(self.label.rect())
        super().resizeEvent(event)

    def clear_rect(self):
        self.rect = QRect()  # ลบค่าสี่เหลี่ยม
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.update()  # อัพเดทการวาด

