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
        self.ui._displayedImg = None
        self.ui.enterButton.clicked.connect(lambda: self._search())
        self.ui.leftButton.clicked.connect(lambda: self._swipeLeft())
        self.ui.rightButton.clicked.connect(lambda: self._swipeRight())

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
            height = pixmapa.height()
            pixmapa = pixmapa.scaledToHeight(min(840, height))
            img.setPixmap(pixmapa)
            prev_response_url = response.url
        self.ui.imgStack.setCurrentIndex(0)
        self.ui._displayedImg = 1
        self.ui.stackedWidget.setCurrentIndex(2)

    def _swipeLeft(self):
        if self.ui._displayedImg == 1:
            return
        else:
            current_page = self.ui._displayedImg - 1
            self.ui.imgStack.setCurrentIndex(current_page - 1)
            self.ui._displayedImg -= 1

    def _swipeRight(self):
        if self.ui._displayedImg == 6:
            return
        else:
            current_page = self.ui._displayedImg - 1
            self.ui.imgStack.setCurrentIndex(current_page + 1)
            self.ui._displayedImg += 1


def guiMain(args):
    app = QtWidgets.QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
