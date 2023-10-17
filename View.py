from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class CalculatorView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create a grid layout for buttons
        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        # Create and style the input field
        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("font-size: 24px; background-color: #000; color: #fff; border: none;")
        self.input_field.setAlignment(Qt.AlignRight)
        grid_layout.addWidget(self.input_field, 0, 0, 1, 4)

        # Define button labels, their positions in the grid, and background colors
        buttons = [
            ('7', 1, 0, '#e18f14'), ('8', 1, 1, '#e18f14'), ('9', 1, 2, '#e18f14'), ('/', 1, 3, '#2196F3'),
            ('4', 2, 0, '#e18f14'), ('5', 2, 1, '#e18f14'), ('6', 2, 2, '#e18f14'), ('*', 2, 3, '#2196F3'),
            ('1', 3, 0, '#e18f14'), ('2', 3, 1, '#e18f14'), ('3', 3, 2, '#e18f14'), ('-', 3, 3, '#2196F3'),
            ('0', 4, 0, '#e18f14'), ('C', 4, 1, '#FF5722'), ('=', 4, 2, '#fff'), ('+', 4, 3, '#2196F3')
        ]

        # Style and add buttons to the grid layout
        for button_text, row, col, color in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet(
                f"font-size: 18px; padding: 10px 20px; background-color: {color}; color: {'#000' if button_text == '=' else '#fff'}; border: none; border-radius: 50%;")
            button.clicked.connect(self.button_clicked)
            grid_layout.addWidget(button, row, col)

        # Adjust the overall appearance
        self.setStyleSheet("background-color: #000;")
        self.setFixedSize(400, 400)
        self.setWindowTitle("Calculator")

    def button_clicked(self):
        button = self.sender()
        if button:
            text = button.text()
            if text == "=":
                expression = self.input_field.text()
                result = self.controller.calculate(expression)
                self.input_field.setText(result)
            elif text == "C":
                self.input_field.clear()
            else:
                current_text = self.input_field.text()
                new_text = current_text + text
                self.input_field.setText(new_text)