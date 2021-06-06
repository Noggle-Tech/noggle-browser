from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QSize

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setFixedSize(QSize(300, 250))
        self.label = QLabel('<h1><strong>ABOUT</strong><hr></h1>Noggle Browser a0.3.1<br><a href="https://github.com/noggle-tech/noggle-browser">Source Code (right click and copy the link)</a><br><br><em>2021 Noggle Technologies</em>')
        layout.addWidget(self.label)
        self.setLayout(layout)