from PySide6.QtCore import QThread, Signal, Slot
from resources.Alert import Alert
from src.ui_DETECTOR_10inch import Ui_MainWindow
from PySide6.QtWidgets import QLabel, QPushButton


class Keyboard(QThread):
    get = Signal(dict)

    def __init__(self, window: Ui_MainWindow):
        super().__init__()
        self.window = window
        self.current_value = ""
        self.max_range = 10  # max range
        self.current_widget = None  # current widget number

        ##########################   Keyboard   ##########################
        self.window.key_1.clicked.connect(lambda: self.read_key("1"))
        self.window.key_2.clicked.connect(lambda: self.read_key("2"))
        self.window.key_3.clicked.connect(lambda: self.read_key("3"))
        self.window.key_4.clicked.connect(lambda: self.read_key("4"))
        self.window.key_5.clicked.connect(lambda: self.read_key("5"))
        self.window.key_6.clicked.connect(lambda: self.read_key("6"))
        self.window.key_7.clicked.connect(lambda: self.read_key("7"))
        self.window.key_8.clicked.connect(lambda: self.read_key("8"))
        self.window.key_9.clicked.connect(lambda: self.read_key("9"))
        self.window.key_0.clicked.connect(lambda: self.read_key("0"))
        self.window.key_backslash.clicked.connect(lambda: self.read_key("/"))
        self.window.key_backspace.clicked.connect(lambda: self.read_key("backspace"))
        self.window.key_enter.clicked.connect(lambda: self.read_key("enter"))
        self.window.key_cancel.clicked.connect(lambda: self.read_key("cancel"))

        ##########################   Events   ##########################
        self.initial_text = self.window.lot_set.text()
        self.initial_style = self.window.lot_set.styleSheet()
        self.window.lot_set.clicked.connect(lambda: self._input(self.window.lot_set))
        self.window.mfg_set.clicked.connect(lambda: self._input(self.window.mfg_set))
        self.window.exp_set.clicked.connect(lambda: self._input(self.window.exp_set))

    # ป้อนข้อมูล
    def _input(self, object: QPushButton):
        self.current_widget: QPushButton = object
        _object = object.objectName()
        _objectValue = object.text()

        self.window.keyboard_title.setText(f"ตั้งค่า {_object.replace('_set', '').upper()}")
        self.window.stackedWidget.setCurrentWidget(self.window.keyboard)

        self.window.val_input.setText(_objectValue)
        if _objectValue != "XXXXXX":
            self.current_value = _objectValue

    # อ่านข้อมูลจาก widgets keyboard
    def read_key(self, key: str):
        if key == "enter":
            value = self.current_value
            if len(value):
                self.current_widget.setText(f"{value}")
                self.window.stackedWidget.setCurrentWidget(self.window.lme_settings_page)
                self.current_value = ""
                self.window.val_input.setText("XXXXXX")
        elif key == "cancel":
            self.window.stackedWidget.setCurrentWidget(self.window.lme_settings_page)
            self.current_value = ""
            self.window.val_input.setText("XXXXXX")
        elif key == "backspace":
            if len(self.current_value) > 0:
                self.current_value = self.current_value[:-1]
                self.window.val_input.setText(self.current_value)
                if len(self.current_value) == 0:
                    self.window.val_input.setText("XXXXXX")
        else:
            if len(self.current_value) < self.max_range:
                self.current_value += key
                self.window.val_input.setText(self.current_value)
