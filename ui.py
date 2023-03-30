from configparser import ConfigParser
from PyQt6 import QtCore, QtWidgets
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from custom_class.CButtonScan import CButtonScan
from custom_class.CProxyModel import CProxyModel
import PyQt6.QtGui
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, WEIGHT, HEIGHT):
        self.WEIGHT = WEIGHT
        self.HEIGHT = HEIGHT
        self.LAYOUT_ROOT = None
        self.BUTTON_SCAN = None
        self.BUTTON_SAVE = None
        self.BUTTON_CLEAR_TABLE = None
        self.LINE_INTER = None
        self.LINE_IP = None
        self.TABLE_HISTORY_MODEL = None
        self.TABLE_IP_MODEL = None
        self.TABLE_HISTORY = None
        self.TABLE_IP = None
        self.LINE_FILTER_NAME = None
        self.LINE_FILTER_CODE = None
        self.LINE_FILTER_INTER = None
        self.LINE_FILTER_IP = None
        self.LINE_FILTER_DOMAIN = None
        self.WALLPAPER = None
        self.WALLPAPER_GLASS = None
        self.FILTER_PROXY_MODEL = None
        self.LABEL_HOST_SCORE = None
        self.LABEL_INFO_WALLPAPER = None
        self.LABEL_TIMER = None

        self.CONFIG = ConfigParser()
        self.CONFIG.read('config.ini')
        super().__init__()

    def setupUi(self, Main):
        Main.setObjectName("MainWindow")
        Main.setFixedSize(self.WEIGHT, self.HEIGHT)
        Main.setAutoFillBackground(False)
        Main.setWindowOpacity(0.96)
        Main.setAutoFillBackground(False)

        self.LAYOUT_ROOT = QtWidgets.QWidget(Main)
        self.LAYOUT_ROOT.resize(self.WEIGHT, self.HEIGHT)
        self.LAYOUT_ROOT.setStyleSheet(open('style/layout/LAYOUT_ROOT.css').read())

        self.WALLPAPER = QLabel(self.LAYOUT_ROOT)
        self.WALLPAPER.setGeometry(QtCore.QRect(0, 0, self.WEIGHT, self.HEIGHT))
        self.WALLPAPER.setPixmap(QPixmap(self.CONFIG.get('wallpaper', 'path')))
        self.WALLPAPER.setScaledContents(True)

        self.WALLPAPER_GLASS = QtWidgets.QWidget(self.LAYOUT_ROOT)
        self.WALLPAPER_GLASS.setGeometry(0, 0, self.WEIGHT, self.HEIGHT)
        self.WALLPAPER_GLASS.setStyleSheet(f"background: rgba{self.CONFIG.get('wallpaper', 'color')}")

        self.LINE_IP = QtWidgets.QLineEdit(self.LAYOUT_ROOT)
        self.LINE_IP.setPlaceholderText("Type IP")
        self.LINE_IP.setStyleSheet(open("style/line_edit/LINE_EDIT_STANDARD.css").read())
        self.LINE_IP.setGeometry(30, 30, 120, 30)

        self.BUTTON_SCAN = CButtonScan(self.LAYOUT_ROOT)
        self.BUTTON_SCAN.setGeometry(180, 30, 30, 30)
        self.BUTTON_SCAN.setIcon(QIcon("res/icon/start.png"))
        self.BUTTON_SCAN.setIconSize(QtCore.QSize(25, 25))
        self.BUTTON_SCAN.setCursor(Qt.CursorShape.PointingHandCursor)

        self.BUTTON_CLEAR_TABLE = QtWidgets.QPushButton(self.LAYOUT_ROOT)
        self.BUTTON_CLEAR_TABLE.setGeometry(220, 30, 30, 30)
        self.BUTTON_CLEAR_TABLE.setIcon(QIcon("res/icon/trash.png"))
        self.BUTTON_CLEAR_TABLE.setIconSize(QtCore.QSize(20, 20))
        self.BUTTON_CLEAR_TABLE.setCursor(Qt.CursorShape.PointingHandCursor)

        self.TABLE_HISTORY_MODEL = PyQt6.QtGui.QStandardItemModel()
        self.TABLE_HISTORY = QtWidgets.QTableView(self.LAYOUT_ROOT)
        self.TABLE_HISTORY.setGeometry(950, 80, 230, 470)
        self.TABLE_HISTORY.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.TABLE_HISTORY.verticalHeader().setVisible(False)
        self.TABLE_HISTORY.setShowGrid(False)
        self.TABLE_HISTORY.setAlternatingRowColors(True)
        self.TABLE_HISTORY.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.TABLE_HISTORY.setStyleSheet(open("style/table/TABLE_IP.css").read())
        self.TABLE_HISTORY.horizontalHeader().setStyleSheet(open("style/table/TABLE_IP_HEAD.css").read())
        self.TABLE_HISTORY.verticalScrollBar().setStyleSheet(open("style/table/TABLE_IP_SLIDER.css").read())
        self.TABLE_HISTORY.setModel(self.TABLE_HISTORY_MODEL)

        self.LINE_INTER = QtWidgets.QLineEdit(self.LAYOUT_ROOT)
        self.LINE_INTER.setGeometry(390, 30, 300, 30)
        self.LINE_INTER.setPlaceholderText("Type Interesting Word")
        self.LINE_INTER.setStyleSheet(open("style/line_edit/LINE_EDIT_STANDARD.css").read())
        self.LINE_INTER.setText("password, login")

        self.BUTTON_SAVE = QtWidgets.QPushButton(self.LAYOUT_ROOT)
        self.BUTTON_SAVE.setGeometry(700, 30, 30, 30)
        self.BUTTON_SAVE.setIcon(QIcon("res/icon/save.png"))
        self.BUTTON_SAVE.setIconSize(QtCore.QSize(25, 25))
        self.BUTTON_SAVE.setCursor(Qt.CursorShape.PointingHandCursor)

        self.LABEL_HOST_SCORE = QtWidgets.QLabel(self.LAYOUT_ROOT)
        self.LABEL_HOST_SCORE.setGeometry(30, 520, 200, 100)
        self.LABEL_HOST_SCORE.setStyleSheet(open("style/label/LABEL_INFO.css").read())
        self.LABEL_HOST_SCORE.setText(f"Find hosts:{' '*2}0")

        self.LABEL_TIMER = QtWidgets.QLabel(self.LAYOUT_ROOT)
        self.LABEL_TIMER.setGeometry(150, 520, 200, 100)
        self.LABEL_TIMER.setStyleSheet(open("style/label/LABEL_INFO.css").read())
        self.LABEL_TIMER.setText(f"Past time:{' '*2}00:00:00")

        self.LABEL_INFO_WALLPAPER = QtWidgets.QLabel(self.LAYOUT_ROOT)
        self.LABEL_INFO_WALLPAPER.setGeometry(1150, 560, 18, 18)
        self.LABEL_INFO_WALLPAPER.setPixmap(QPixmap("res/icon/info.png"))
        self.LABEL_INFO_WALLPAPER.setToolTip("Press 'Alt' to change the wallpaper")
        self.LABEL_INFO_WALLPAPER.setScaledContents(True)

        self.TABLE_IP = QtWidgets.QTableView(self.LAYOUT_ROOT)
        self.TABLE_IP.setGeometry(30, 100, 900, 450)
        self.TABLE_IP.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.TABLE_IP.setSortingEnabled(True)
        self.TABLE_IP.verticalHeader().setVisible(False)
        self.TABLE_IP.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.TABLE_IP.setStyleSheet(open("style/table/TABLE_IP.css").read())
        self.TABLE_IP.horizontalHeader().setStyleSheet(open("style/table/TABLE_IP_HEAD.css").read())
        self.TABLE_IP.verticalScrollBar().setStyleSheet(open("style/table/TABLE_IP_SLIDER.css").read())
        self.TABLE_IP.verticalHeader().setVisible(False)
        self.TABLE_IP.setShowGrid(False)
        self.TABLE_IP.setAlternatingRowColors(True)
        self.TABLE_IP_MODEL = PyQt6.QtGui.QStandardItemModel()

        self.FILTER_PROXY_MODEL = CProxyModel()
        self.FILTER_PROXY_MODEL.setSourceModel(self.TABLE_IP_MODEL)

        for row_item in range(30, 930, 180):
            LINE_FILTER_NO_NAME = QtWidgets.QLineEdit(self.LAYOUT_ROOT)
            LINE_FILTER_NO_NAME.setStyleSheet(open("style/line_edit/LINE_EDIT_FILTER.css").read())
            LINE_FILTER_NO_NAME.setGeometry(row_item, 80, 180, 20)
            LINE_FILTER_NO_NAME.setPlaceholderText(f"{' '*4}filter")
            LINE_FILTER_NO_NAME.textChanged.connect(lambda getText, column=row_item/180:
                                                    self.FILTER_PROXY_MODEL.
                                                    setFilterByColumn(getText, column))

        self.TABLE_IP.setModel(self.FILTER_PROXY_MODEL)
        self.translateUi(Main)

    def translateUi(self, Main):
        self.TABLE_IP_MODEL.setHorizontalHeaderLabels(['IP', 'DOMAIN', 'NAME', 'CODE', 'INTER'])
        self.TABLE_HISTORY_MODEL.setHorizontalHeaderLabels(['INP', 'OUT'])
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("MainWindow", f"Emilia"))
