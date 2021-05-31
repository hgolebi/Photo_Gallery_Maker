from io import BytesIO
from PhotoGalleryMaker import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import requests
from PIL import Image
import sys

url = 'https://source.unsplash.com/featured/?{KEYWORD}'

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui._imgList = [
            self.ui.img1,
            self.ui.img2,
            self.ui.img3,
            self.ui.img4,
            self.ui.img5,
            self.ui.img6,
        ]
        self.ui.enterButton.clicked.connect(lambda: self._search())

    # def _getPhoto(self, keyword):
    #     response = requests.get(url.format(KEYWORD=keyword))
    #     img_bytes = BytesIO(response.content)
    #     return img_bytes

    def _search(self):
        text = self.ui.writeKeyword.text()
        for img in self.ui._imgList:
            pixmapa = QtGui.QPixmap()
            response = requests.get(url.format(KEYWORD=text))
            if img is self.ui.img1:
                prev_response_url = ''
            while prev_response_url == response.url:
                response = requests.get(url.format(KEYWORD=text))
            img_bytes = BytesIO(response.content)
            pixmapa.loadFromData(img_bytes.getvalue())
            img.setPixmap(pixmapa)
            prev_response_url = response.url
        self.ui.stackedWidget.setCurrentIndex(1)


def guiMain(args):
    app = QtWidgets.QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()

if __name__ == "__main__":
    guiMain(sys.argv)