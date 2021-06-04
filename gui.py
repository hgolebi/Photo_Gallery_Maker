from io import BytesIO
from PhotoGalleryMaker import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import os
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
        self.ui._collageList = [
            self.ui.collageImg1,
            self.ui.collageImg2,
            self.ui.collageImg3,
            self.ui.collageImg4,
            self.ui.collageImg5,
            self.ui.collageImg6,
        ]
        self.ui.enterButton.clicked.connect(lambda: self._search())
        self.ui.leftButton.clicked.connect(lambda: self._swipeLeft())
        self.ui.rightButton.clicked.connect(lambda: self._swipeRight())
        self.ui.rotLeftButton.clicked.connect(lambda: self._rotate("L"))
        self.ui.rotRightButton.clicked.connect(lambda: self._rotate("R"))
        self.ui.blurredBox.stateChanged.connect(lambda: self._Blur())
        self.ui.black_whiteBox.stateChanged.connect(lambda: self._BlackAndWhite())
        self.ui.saveButton.clicked.connect(lambda: self._saveImage())
        self.ui.collageButton.clicked.connect(lambda: self._createCollage())
        self.ui.returnButton.clicked.connect(lambda: self._setPage(2))
        self.ui.backButton.clicked.connect(lambda: self._setPage(0))
        self.ui.galleryButton.clicked.connect(lambda: self._setPage(2))

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
            img.is_Blurred = False
            img.is_BlackAndWhite = False
            pixmap.loadFromData(img_bytes.getvalue())
            height = pixmap.height()
            pixmap = pixmap.scaledToHeight(min(800, height))
            img.setPixmap(pixmap)
            prev_response_url = response.url
        self.ui.imgStack.setCurrentIndex(0)
        self.ui._displayedImg = 0
        self.ui.blurredBox.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.ui.black_whiteBox.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.galleryButton.setEnabled(True)

    def _setCheckboxes(self):
        if self.ui._imgList[self.ui._displayedImg].is_Blurred:
            self.ui.blurredBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ui.blurredBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ui._imgList[self.ui._displayedImg].is_BlackAndWhite:
            self.ui.black_whiteBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ui.black_whiteBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def _swipeLeft(self):
        if self.ui._displayedImg == 0:
            return
        else:
            current_page = self.ui._displayedImg
            self.ui.imgStack.setCurrentIndex(current_page - 1)
            self.ui._displayedImg -= 1
            self._setCheckboxes()

    def _swipeRight(self):
        if self.ui._displayedImg == 5:
            return
        else:
            current_page = self.ui._displayedImg
            self.ui.imgStack.setCurrentIndex(current_page + 1)
            self.ui._displayedImg += 1
            self._setCheckboxes()

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

    def _Blur(self):
        is_checked = self.ui.blurredBox.isChecked()
        image = self.ui._imgList[self.ui._displayedImg]
        if is_checked is True:
            image.is_Blurred = True
            image.PIL_image = image.PIL_image.filter(ImageFilter.GaussianBlur(4))

        else:
            image.is_Blurred = False
            image.PIL_image = image.orginal_PIL_image.rotate(image.angle, expand=1)
            if image.is_BlackAndWhite:
                image.PIL_image = image.PIL_image.convert("L")

        img_bytes = BytesIO()
        image.PIL_image.save(img_bytes, format='PNG')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(img_bytes.getvalue())
        height = pixmap.height()
        pixmap = pixmap.scaledToHeight(min(800, height))
        image.setPixmap(pixmap)

    def _BlackAndWhite(self):
        is_checked = self.ui.black_whiteBox.isChecked()
        image = self.ui._imgList[self.ui._displayedImg]
        if is_checked is True:
            image.is_BlackAndWhite = True
            image.PIL_image = image.PIL_image.convert("L")
        else:
            image.is_BlackAndWhite = False
            image.PIL_image = image.orginal_PIL_image.rotate(image.angle, expand=1)
            if image.is_Blurred:
                image.PIL_image = image.PIL_image.filter(ImageFilter.GaussianBlur(4))
        img_bytes = BytesIO()
        image.PIL_image.save(img_bytes, format='PNG')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(img_bytes.getvalue())
        height = pixmap.height()
        pixmap = pixmap.scaledToHeight(min(800, height))
        image.setPixmap(pixmap)

    def _saveImage(self):
        dir_name = self.ui.writeKeyword.text() + "_gallery"
        if dir_name not in os.listdir('.'):
            os.mkdir(dir_name)
        img_count = len(os.listdir('.\\' + dir_name))
        image = self.ui._imgList[self.ui._displayedImg]
        img_name = image.objectName()
        image.PIL_image.save(f'.\\{dir_name}\\img{img_count + 1}.png')

    def _createCollage(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        index = 0
        for img in self.ui._imgList:
            img_bytes = BytesIO()
            img.PIL_image.save(img_bytes, format='PNG')
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(img_bytes.getvalue())
            pixmap = pixmap.scaledToHeight(400)
            self.ui._collageList[index].setPixmap(pixmap)
            index += 1

    def _setPage(self, page):
        self.ui.stackedWidget.setCurrentIndex(page)



def guiMain(args):
    app = QtWidgets.QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
