from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import QEvent, Qt, QRect, QPoint, Signal
from resources.Camera import RectangleSettings


class Rectangle(QWidget):
    rect_drawn = Signal(int, int, int, int)

    def __init__(self, label: QLabel):
        super().__init__(label)
        self.label = label
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.setGeometry(self.label.rect())
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.drawing = False
        self.rect = QRect()

    def get_image_position(self, pos: QPoint):
        """Convert widget position to image position"""
        pixmap = self.label.pixmap()
        if not pixmap:
            return pos

        # Get label and pixmap dimensions
        label_width = self.label.width()
        label_height = self.label.height()
        pixmap_width = pixmap.width()
        pixmap_height = pixmap.height()

        # Calculate scaling factors
        w_scale = pixmap_width / label_width
        h_scale = pixmap_height / label_height

        # Calculate actual image position in label
        scaled_width = pixmap_width / w_scale
        scaled_height = pixmap_height / h_scale

        # Calculate offsets (for centered images)
        x_offset = (label_width - scaled_width) / 2
        y_offset = (label_height - scaled_height) / 2

        # Adjust position relative to image
        x = (pos.x() - x_offset) * w_scale
        y = (pos.y() - y_offset) * h_scale

        # Make sure position is within image bounds
        x = max(0, min(x, pixmap_width))
        y = max(0, min(y, pixmap_height))

        return QPoint(int(x), int(y))

    def set_rectangle_from_image_coords(self, rect: RectangleSettings):
        """Set rectangle from image coordinates"""
        self.rect = QRect(QPoint(rect.X1, rect.Y1), QPoint(rect.X2, rect.Y2)).normalized()
        self.update()

    def eventFilter(self, obj, event):
        if obj == self.label:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.start_point = self.get_image_position(event.position().toPoint())
                self.end_point = self.start_point
                self.drawing = True
                self.update()
                return True

            elif event.type() == QEvent.MouseMove and self.drawing:
                self.end_point = self.get_image_position(event.position().toPoint())
                self.update()
                return True

            elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self.end_point = self.get_image_position(event.position().toPoint())
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

            # Convert image coordinates back to widget coordinates for drawing
            pixmap = self.label.pixmap()
            if pixmap:
                label_width = self.label.width()
                label_height = self.label.height()
                pixmap_width = pixmap.width()
                pixmap_height = pixmap.height()

                w_scale = label_width / pixmap_width
                h_scale = label_height / pixmap_height

                scaled_width = pixmap_width * w_scale
                scaled_height = pixmap_height * h_scale

                x_offset = (label_width - scaled_width) / 2
                y_offset = (label_height - scaled_height) / 2

                if self.drawing:
                    start_x = self.start_point.x() * w_scale + x_offset
                    start_y = self.start_point.y() * h_scale + y_offset
                    end_x = self.end_point.x() * w_scale + x_offset
                    end_y = self.end_point.y() * h_scale + y_offset
                    rect = QRect(QPoint(start_x, start_y), QPoint(end_x, end_y)).normalized()
                else:
                    rect_x = self.rect.x() * w_scale + x_offset
                    rect_y = self.rect.y() * h_scale + y_offset
                    rect_width = self.rect.width() * w_scale
                    rect_height = self.rect.height() * h_scale
                    rect = QRect(rect_x, rect_y, rect_width, rect_height)

                painter.drawRect(rect)

    def resizeEvent(self, event):
        self.setGeometry(self.label.rect())
        super().resizeEvent(event)

    def clear_rect(self):
        self.rect = QRect()
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.update()
