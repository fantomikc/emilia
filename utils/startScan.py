import requests
from threading import Thread
from PyQt6 import QtCore
from bs4 import BeautifulSoup
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import contextlib

urllib3.disable_warnings(InsecureRequestWarning)


class startScan(QtCore.QThread):
    find = QtCore.pyqtSignal(list)

    def __init__(self, ip, interesting_word, parent=None):
        super().__init__(parent)
        self.interesting_word = interesting_word
        self.list_ip = ip.split(".")
        self.ip = list(map(int, self.list_ip))

    def run(self):
        while True:
            if self.ip[3] >= 256:
                self.ip[3] = 0
                self.ip[2] += 1

            if self.ip[2] >= 256:
                self.ip[2] = 0
                self.ip[1] += 1

            if self.ip[1] >= 256:
                self.ip[1] = 0
                self.ip[0] += 1

            self.ip[3] += 1

            thread = Thread(target=self.startScanner, args={f"{'.'.join(map(str, self.ip))}"})
            thread.start()

    def startScanner(self, input_ip):
        with contextlib.suppress(Exception):
            response = requests.get(f"http://{input_ip}", timeout=3, verify=False)
            status_code = response.status_code

            output_ip = response.url.split('/')[2]
            domain = output_ip if input_ip not in output_ip else ""
            soup_text = BeautifulSoup(response.text, "html.parser")
            title = soup_text.find("title").string

            interesting_word = [item for item in self.interesting_word if response.text.lower().__contains__(item)]
            interesting_word = ':'.join(interesting_word)

            self.find.emit([input_ip, domain, title, status_code, interesting_word])
