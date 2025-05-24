from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QSizePolicy
from PySide6.QtCore import Qt

class VirtualKeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Keyboard")
        self.shift = False
        
        main_layout = QVBoxLayout()
        
        # Create a text input field
        self.text_input = QLineEdit()
        main_layout.addWidget(self.text_input)
        
        # Keyboard layout
        keyboard_layout = QVBoxLayout()
        
        # Define keys layout
        keys_layout = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Shift", "Z", "X", "C", "V", "B", "N", "M", "Backspace"],
            ["Space", "Enter"]
        ]
        
        for row in keys_layout:
            row_layout = QHBoxLayout()
            for key in row:
                button = QPushButton(key)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                button.clicked.connect(self.button_clicked)
                row_layout.addWidget(button)
            keyboard_layout.addLayout(row_layout)
        
        main_layout.addLayout(keyboard_layout)
        self.setLayout(main_layout)
    
    def button_clicked(self):
        button = self.sender()
        key_text = button.text()
        
        if key_text == "Space":
            self.text_input.insert(" ")
        elif key_text == "Backspace":
            self.text_input.backspace()
        elif key_text == "Enter":
            self.text_input.insert("\n")
        elif key_text == "Shift":
            self.shift = not self.shift
            self.update_shift()
        else:
            if self.shift:
                self.text_input.insert(key_text.upper())
            else:
                self.text_input.insert(key_text.lower())
    
    def update_shift(self):
        # Update button texts based on shift state
        for button in self.findChildren(QPushButton):
            if button.text().isalpha():
                if self.shift:
                    button.setText(button.text().upper())
                else:
                    button.setText(button.text().lower())

if __name__ == "__main__":
    app = QApplication([])
    keyboard = VirtualKeyboard()
    keyboard.show()
    app.exec()
