from io import BytesIO
from PhotoGalleryMaker import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import requests
from PIL import Image, ImageFilter
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
        self.ui.rotLeftButton.clicked.connect(lambda: self._rotate("L"))
        self.ui.rotRightButton.clicked.connect(lambda: self._rotate("R"))
        self.ui.blurredBox.stateChanged.connect(lambda: self._changeBlur())

    def _search(self):
        text = self.ui.writeKeyword.text()
        for img in self.ui._imgList:
            pixmap = QtGui.QPixmap()
            response = requests.get(url.format(KEYWORD=text))
            if img is self.ui.img1:
                prev_response_url = ''
            while prev_response_url == response.url:
                response = requests.get(url.format(KEYWORD=text))
            img_bytes = BytesIO(response.content)
            img.PIL_image = Image.open(img_bytes)
            img.orginal_PIL_image = img.PIL_image
            img.angle = 0
            pixmap.loadFromData(img_bytes.getvalue())
            height = pixmap.height()
            pixmap = pixmap.scaledToHeight(min(800, height))
            img.setPixmap(pixmap)
            prev_response_url = response.url
        self.ui.imgStack.setCurrentIndex(0)
        self.ui._displayedImg = 0
        self.ui.stackedWidget.setCurrentIndex(2)

    def _swipeLeft(self):
        if self.ui._displayedImg == 0:
            return
        else:
            current_page = self.ui._displayedImg
            self.ui.imgStack.setCurrentIndex(current_page - 1)
            self.ui._displayedImg -= 1

    def _swipeRight(self):
        if self.ui._displayedImg == 5:
            return
        else:
            current_page = self.ui._displayedImg
            self.ui.imgStack.setCurrentIndex(current_page + 1)
            self.ui._displayedImg += 1

    def _rotate(self, direction):
        image = self.ui._imgList[self.ui._displayedImg]

        if direction == "L":
            image.PIL_image = image.PIL_image.rotate(90, expand=1)
            image.angle += 90
        elif direction == "R":
            image.PIL_image = image.PIL_image.rotate(-90, expand=1)
            image.angle -= 90
        else:
            raise ValueError("Direction has to be 'L' or 'R'")
        img_bytes = BytesIO()
        image.PIL_image.save(img_bytes, format='PNG')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(img_bytes.getvalue())
        height = pixmap.height()
        pixmap = pixmap.scaledToHeight(min(800, height))
        image.setPixmap(pixmap)

    def _changeBlur(self):
        is_checked = self.ui.blurredBox.isChecked()
        image = self.ui._imgList[self.ui._displayedImg]
        if is_checked is True:
            image.PIL_image = image.PIL_image.filter(ImageFilter.GaussianBlur(4))
        else:
            image.PIL_image = image.orginal_PIL_image.rotate(image.angle)
        img_bytes = BytesIO()
        image.PIL_image.save(img_bytes, format='PNG')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(img_bytes.getvalue())
        height = pixmap.height()
        pixmap = pixmap.scaledToHeight(min(800, height))
        image.setPixmap(pixmap)


def guiMain(args):
    app = QtWidgets.QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
