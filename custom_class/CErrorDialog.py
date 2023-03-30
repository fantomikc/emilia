from PyQt6.QtWidgets import QMessageBox


class CErrorDialog(QMessageBox):
    def __init__(self, message, title="Error"):
        super().__init__()
        self.setIcon(QMessageBox.Icon.Critical)
        self.setText(message)
        self.setWindowTitle(title)
        self.exec()
