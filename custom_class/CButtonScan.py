from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon


class CButtonScan(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bool = False

    def click(self):
        self.bool = not self.bool
        if self.bool:
            self.setIcon(QIcon('res/icon/stop.png'))
        else:
            self.setIcon(QIcon('res/icon/start.png'))
