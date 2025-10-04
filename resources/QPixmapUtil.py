import cv2
import numpy as np
from PySide6.QtGui import QImage, QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt, QSize

class QPixmapUtil:
    @staticmethod
    def from_cvimg(cv_img: np.ndarray, size: QSize = None, radius: int = 20) -> QPixmap:
        """
        ประสิทธิภาพสูง: แปลง OpenCV image -> QPixmap พร้อมปรับขนาดและมุมโค้ง
        """
        # 1. ปรับขนาดด้วย OpenCV ก่อน
        if size is not None:
            target_w, target_h = size.width(), size.height()
            h, w = cv_img.shape[:2]

            scale = max(target_w / w, target_h / h)  # cover
            new_w, new_h = int(w * scale), int(h * scale)
            cv_img = cv2.resize(cv_img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

            # crop center
            start_x = (new_w - target_w) // 2
            start_y = (new_h - target_h) // 2
            cv_img = cv_img[start_y:start_y+target_h, start_x:start_x+target_w]

        # 2. แปลง BGR -> RGB
        if cv_img.ndim == 2:
            qimg = QImage(cv_img.data, cv_img.shape[1], cv_img.shape[0],
                          cv_img.shape[1], QImage.Format.Format_Grayscale8)
        else:
            rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
            qimg = QImage(rgb.data, rgb.shape[1], rgb.shape[0],
                          3 * rgb.shape[1], QImage.Format.Format_RGB888)

        # 3. ทำมุมโค้งด้วย alpha mask (fast)
        if radius > 0:
            h, w = qimg.height(), qimg.width()
            mask = QImage(w, h, QImage.Format.Format_Alpha8)
            mask.fill(0)
            painter = QPainter(mask)
            path = QPainterPath()
            path.addRoundedRect(0, 0, w, h, radius, radius)
            painter.fillPath(path, Qt.GlobalColor.white)
            painter.end()
            qimg.setAlphaChannel(mask)

        return QPixmap.fromImage(qimg)
