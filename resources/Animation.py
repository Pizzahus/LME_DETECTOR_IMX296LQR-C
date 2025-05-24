from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QObject
from PySide6.QtWidgets import QGraphicsOpacityEffect, QWidget

class AnimatedWidgetHelper(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animations = {}

    def _ensure_effect_exists(self, widget: QWidget):
        """ตรวจสอบและสร้าง effect หากยังไม่มี"""
        if widget not in self._animations:
            effect = QGraphicsOpacityEffect(widget)
            widget.setGraphicsEffect(effect)
            animation = QPropertyAnimation(effect, b"opacity", self)
            animation.setEasingCurve(QEasingCurve.InOutQuad)
            self._animations[widget] = (effect, animation)
        return self._animations[widget]

    def fade_widget(self, widget: QWidget, show: bool, duration: int = 300):
        effect, animation = self._ensure_effect_exists(widget)

        animation.stop()
        animation.setDuration(duration)

        # วิธีที่ 1: ใช้ try-except เพื่อดักจับ RuntimeError (แนะนำ)
        try:
            animation.finished.disconnect()
        except (TypeError, RuntimeError):
            pass

        if show:
            # ตั้งค่า opacity เป็น 0 ก่อนแสดง (ถ้า widget ถูกซ่อนอยู่)
            if not widget.isVisible():
                effect.setOpacity(0.0)
            widget.setVisible(True)  # แสดง widget ก่อนเริ่ม animation
            animation.setStartValue(effect.opacity())  # เริ่มจากค่าปัจจุบัน
            animation.setEndValue(1.0)
        else:
            animation.setStartValue(effect.opacity())  # เริ่มจากค่าปัจจุบัน
            animation.setEndValue(0.0)

            def hide_after():
                widget.setVisible(False)
            animation.finished.connect(hide_after)

        animation.start()