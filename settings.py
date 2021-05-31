from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QSize
import sys


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setFixedSize(QSize(250, 100))
        self.label = QLabel("ABOUT\n\nNoggle Browser a0.2\n\n2021 Noggle Technologies")
        layout.addWidget(self.label)
        self.setLayout(layout)