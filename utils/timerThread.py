from PyQt6 import QtCore
from itertools import count
from time import sleep


class timerThread(QtCore.QThread):
    timer = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        for second in count(1):
            sleep(1)
            self.convertTimer(second)

    def convertTimer(self, second):
        minutes, second = divmod(second, 60)
        hours, minutes = divmod(minutes, 60)

        self.timer.emit(f"{hours:02}:{minutes:02}:{second:02}")
