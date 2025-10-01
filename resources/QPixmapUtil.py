import cv2
import numpy as np
from PySide6.QtGui import QImage, QPixmap, QPainter, QPainterPath, QPen
from PySide6.QtCore import Qt


class QPixmapUtil:
    @staticmethod
    def from_cvimg(cv_img: np.ndarray, radius: int = 30,
                   border: bool = False, border_color=Qt.GlobalColor.black, border_width: int = 2) -> QPixmap:
        """
        แปลง OpenCV image -> QPixmap พร้อมขอบโค้ง (rounded corners)

        Args:
            cv_img (np.ndarray): OpenCV image
            radius (int): รัศมีความโค้งของมุม
            border (bool): วาดเส้นขอบด้วยหรือไม่
            border_color: สีขอบ (ใช้ Qt.GlobalColor หรือ QColor)
            border_width (int): ความหนาของเส้นขอบ

        Returns:
            QPixmap: pixmap พร้อมขอบโค้ง
        """
        # แปลง OpenCV image -> QImage
        if cv_img.ndim == 2:
            h, w = cv_img.shape
            qimg = QImage(cv_img.data, w, h, w, QImage.Format.Format_Grayscale8)
        else:
            h, w, ch = cv_img.shape
            rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format.Format_RGB888)

        pixmap = QPixmap.fromImage(qimg)

        # วาดลงบน pixmap โปร่งใส
        rounded = QPixmap(pixmap.size())
        rounded.fill(Qt.GlobalColor.transparent)

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(0, 0, pixmap.width(), pixmap.height(), radius, radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)

        # ถ้ามีขอบ
        if border:
            pen = QPen(border_color, border_width)
            painter.setPen(pen)
            painter.drawPath(path)

        painter.end()
        return rounded
