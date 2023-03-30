import sys
import os
import PyQt6
from PyQt6.QtGui import QPixmap
from custom_class.CErrorDialog import CErrorDialog
from ui import MainWindow
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from utils.startScan import startScan
from utils.sqlSave import sqlSave
from utils.timerThread import timerThread
from PyQt6.QtCore import Qt
import random


class Emilia(QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = MainWindow(1200, 600)
        self.ui.setupUi(self)

        self.ui.FILTER_PROXY_MODEL.count.connect(self.setHostScore)
        self.ui.BUTTON_SAVE.clicked.connect(self.getPath)
        self.ui.BUTTON_CLEAR_TABLE.clicked.connect(self.clearTable)
        self.ui.BUTTON_SCAN.clicked.connect(self.onScanButtonClick)
        self.thread_time = None
        self.thread_scan = None

    def onScanButtonClick(self):
        self.ui.BUTTON_SCAN.click()
        if self.ui.BUTTON_SCAN.bool:
            if not self.verifierIP():
                self.ui.BUTTON_SCAN.click()
                CErrorDialog("Check the correctness of the IP field data")
            else:
                self.thread_scan = startScan(self.ui.LINE_IP.text(), self.ui.LINE_INTER.text().split(", "))
                self.thread_scan.find.connect(self.addItem)
                self.thread_scan.start()
                self.thread_time = timerThread()
                self.thread_time.timer.connect(self.setTime)
                self.thread_time.start()
                self.setHostScore()
        else:
            if self.thread_scan.isRunning():
                self.addHistory()
                self.thread_scan.terminate()
                if self.thread_time.isRunning():
                    self.thread_time.terminate()

    def verifierIP(self):
        ip_check = self.ui.LINE_IP.text().split(".")
        return len(ip_check) == 4 and all(item.isdigit() and 0 <= int(item) < 256 for item in ip_check)

    def addItem(self, answer):
        self.ui.TABLE_IP_MODEL.appendRow([
            PyQt6.QtGui.QStandardItem(str(answer[0])),
            PyQt6.QtGui.QStandardItem(str(answer[1])),
            PyQt6.QtGui.QStandardItem(str(answer[2])),
            PyQt6.QtGui.QStandardItem(str(answer[3])),
            PyQt6.QtGui.QStandardItem(str(answer[4]))])
        self.setHostScore()

    def clearTable(self):
        self.ui.TABLE_IP_MODEL.setRowCount(0)
        self.setHostScore()

    def setHostScore(self):
        self.ui.LABEL_HOST_SCORE.setText(f"Find hosts:{' '*2}{self.ui.TABLE_IP.model().rowCount()}")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Alt:
            list_path = os.listdir("res/wallpaper/")
            path = random.choice(list_path)
            self.updatePathWallpaper(f"res/wallpaper/{path}")

    def getPath(self):
        path_table_save = QFileDialog.getSaveFileName(self, "SAVE TABLE", "data_base", "All Files(*.db)")[0]
        if path_table_save:
            sqlSave(path_table_save, self.ui.TABLE_IP)

    def addHistory(self):
        self.ui.TABLE_HISTORY_MODEL.appendRow([
            PyQt6.QtGui.QStandardItem(str(self.ui.LINE_IP.text())),
            PyQt6.QtGui.QStandardItem(str(".".join(map(str, self.thread_scan.ip))))])

    def setTime(self, answer):
        self.ui.LABEL_TIMER.setText(f"Past time:{' '*2}{answer}")

    def updatePathWallpaper(self, path):
        self.ui.CONFIG.set('wallpaper', 'path', path)
        with open('config.ini', 'w') as file:
            self.ui.CONFIG.write(file)
        self.setWallpaper()

    def setWallpaper(self):
        self.ui.WALLPAPER.setPixmap(QPixmap(self.ui.CONFIG.get('wallpaper', 'path')))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('res/icon/icon.jpg'))
    myapp = Emilia()
    myapp.show()
    sys.exit(app.exec())
