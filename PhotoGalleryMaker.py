from io import BytesIO
from app_GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests
from PIL import Image, ImageFilter
import sys

url = 'https://source.unsplash.com/featured/?{KEYWORD}'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Ui_MainWindow() is a class generated from ui file created in QtDesigner app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        # lists of QLabel objects to enable iteration,
        # imgList is a list of QLabel objects in gallery

        self.ui._imgList = [
            self.ui.img1,
            self.ui.img2,
            self.ui.img3,
            self.ui.img4,
            self.ui.img5,
            self.ui.img6,
        ]
        # collageList is a list of QLabel objects in collage
        self.ui._collageList = [
            self.ui.collageImg1,
            self.ui.collageImg2,
            self.ui.collageImg3,
            self.ui.collageImg4,
            self.ui.collageImg5,
            self.ui.collageImg6,
        ]
        self.ui.wrongKeywordMessege.setVisible(False)

        self.ui.enterButton.clicked.connect(lambda: self._search())
        self.ui.writeKeyword.textChanged.connect(lambda: self._displayMessage(False))
        self.ui.leftButton.clicked.connect(lambda: self._swipeLeft())
        self.ui.rightButton.clicked.connect(lambda: self._swipeRight())
        self.ui.rotLeftButton.clicked.connect(lambda: self._rotate("L"))
        self.ui.rotRightButton.clicked.connect(lambda: self._rotate("R"))
        self.ui.blurredBox.stateChanged.connect(lambda: self._Blur())
        self.ui.black_whiteBox.stateChanged.connect(lambda: self._BlackAndWhite())
        self.ui.saveButton.clicked.connect(lambda: self._saveImage())
        self.ui.collageButton.clicked.connect(lambda: self._createCollage())
        self.ui.returnButton.clicked.connect(lambda: self._setPage(1))
        self.ui.backButton.clicked.connect(lambda: self._setPage(0))
        self.ui.galleryButton.clicked.connect(lambda: self._setPage(1))

    def _search(self):
        ''' Function that takes a keyword given by the user and searches for
        images that match the keyword. It downloads 6 images through
        Unsplash API, sets them as QPixmap and ataches to QLabel objects
        '''
        text = self.ui.writeKeyword.text()
        self.ui.wrongKeywordMessege.setVisible(False)
        for img in self.ui._imgList:
            # Getting image data through https
            response = requests.get(url.format(KEYWORD=text))
            if 'source-404' in response.url:
                self._displayMessage(True)
                return
            if img is self.ui.img1:
                prev_response_url = ''
            # While loop prevents getting same images 2 or more times in a row.
            # It doesn't prevent getting same images e.g. on 1st and 3rd place
            # but this situation is very unlikely and it helps to solve the
            # case where only 5 or less pictures suit a certain keyword.
            while prev_response_url == response.url:
                response = requests.get(url.format(KEYWORD=text))
            # Converting data from URL to BytesIO obcject.
            img_bytes = BytesIO(response.content)
            # Converting bytes object to Pillow Image object.
            # This object isn't nessesary to display in gui but it's needed for
            # later transformations and it storages current version of
            # displayed image to later save it or use it in collage.
            img.PIL_image = Image.open(img_bytes)
            # Creating copy of Pillow Image object to e.g. unblurr a blurred image.
            img.orginal_PIL_image = img.PIL_image
            img.angle = 0
            img.is_Blurred = False
            img.is_BlackAndWhite = False
            # loading BytesIO object to QPixmap.
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(img_bytes.getvalue())
            # Scaling image to fit in displayed window.
            height = pixmap.height()
            pixmap = pixmap.scaledToHeight(min(800, height))
            # Ataching QPixmap to QLabel object.
            img.setPixmap(pixmap)
            prev_response_url = response.url
        # Setting 1st image to display first.
        self.ui.imgStack.setCurrentIndex(0)
        # Atrribute that tells which image is currently displayed.
        self.ui._displayedImg = 0
        # Setting checkboxes to be unchecked by default.
        self.ui.blurredBox.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.ui.black_whiteBox.setCheckState(QtCore.Qt.CheckState.Unchecked)
        # Changing window from starting window to gallery.
        self.ui.stackedWidget.setCurrentIndex(1)
        # Setting 'To Gallery' button to work after first search
        self.ui.galleryButton.setEnabled(True)

    def _displayMessage(self, bool):  # no image found message
        self.ui.wrongKeywordMessege.setVisible(bool)

    def _setCheckboxes(self):
        ''' Function that adjusts checkboxes to the state of image
        e.g if picture is blurred, 'Blurred' checkbox is set to be checked.

            It's nessesary to adjust this checkboxes when switching from one
        image to another.
        '''
        if self.ui._imgList[self.ui._displayedImg].is_Blurred:
            self.ui.blurredBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ui.blurredBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

        if self.ui._imgList[self.ui._displayedImg].is_BlackAndWhite:
            self.ui.black_whiteBox.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.ui.black_whiteBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def _swipeLeft(self):
        ''' Function that changes displayed image to previous image. '''
        if self.ui._displayedImg == 0:
            return
        else:
            current_page = self.ui._displayedImg
            self.ui.imgStack.setCurrentIndex(current_page - 1)
            self.ui._displayedImg -= 1
            self._setCheckboxes()

    def _swipeRight(self):
        ''' Function that changes displayed image to next image. '''
        if self.ui._displayedImg == 5:
            return
        else:
            current_page = self.ui._displayedImg
            self.ui.imgStack.setCurrentIndex(current_page + 1)
            self.ui._displayedImg += 1
            self._setCheckboxes()

    def _rotate(self, direction):
        ''' Fuction that rotates images. First it modifies the Pillow Image
        object and then it turns it into QPixmap that is loaded into QLabel.

        :param direction: 'L' - left, 'R' - right
        '''
        image = self.ui._imgList[self.ui._displayedImg]

        if direction == "L":
            image.PIL_image = image.PIL_image.rotate(90, expand=1)
            image.angle += 90
        if direction == "R":
            image.PIL_image = image.PIL_image.rotate(-90, expand=1)
            image.angle -= 90
        img_bytes = BytesIO()
        # saving transformed Pillow Image to img_bytes (BytesIO object)
        image.PIL_image.save(img_bytes, format='PNG')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(img_bytes.getvalue())
        height = pixmap.height()
        pixmap = pixmap.scaledToHeight(min(800, height))
        image.setPixmap(pixmap)

    def _Blur(self):
        ''' Function that blurres images. First it modifies the Pillow Image
        object and then it turns it into QPixmap that is loaded into QLabel.
        '''
        is_checked = self.ui.blurredBox.isChecked()
        image = self.ui._imgList[self.ui._displayedImg]
        if is_checked is True:
            image.is_Blurred = True
            new_image = image.PIL_image.filter(ImageFilter.GaussianBlur(4))
            image.PIL_image = new_image
        # In order to unblurr the blurred image, we have to use the copy of
        # orginal Pillow Image object. Notice that if the photo was e.g.
        # rotated we have to rotate the copy so it fits what's currently
        # displayed. The same goes with the black and white filter.
        else:
            image.is_Blurred = False
            new_image = image.orginal_PIL_image.rotate(image.angle, expand=1)
            if image.is_BlackAndWhite:
                new_image = new_image.convert("L")
            image.PIL_image = new_image

        img_bytes = BytesIO()
        image.PIL_image.save(img_bytes, format='PNG')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(img_bytes.getvalue())
        height = pixmap.height()
        pixmap = pixmap.scaledToHeight(min(800, height))
        image.setPixmap(pixmap)

    def _BlackAndWhite(self):
        ''' Function that turns image to be black and white.
        First it modifies the Pillow Image object and then it turns
        it into QPixmap that is loaded into QLabel.
        '''
        is_checked = self.ui.black_whiteBox.isChecked()
        image = self.ui._imgList[self.ui._displayedImg]
        if is_checked is True:
            image.is_BlackAndWhite = True
            image.PIL_image = image.PIL_image.convert("L")
        # We're using Pillow Image copy to bring back colours
        # Check _Blurr() documentation for more detailed info
        else:
            image.is_BlackAndWhite = False
            new_image = image.orginal_PIL_image.rotate(image.angle, expand=1)
            if image.is_Blurred:
                new_image = new_image.filter(ImageFilter.GaussianBlur(4))
            image.PIL_image = new_image

        img_bytes = BytesIO()
        image.PIL_image.save(img_bytes, format='PNG')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(img_bytes.getvalue())
        height = pixmap.height()
        pixmap = pixmap.scaledToHeight(min(800, height))
        image.setPixmap(pixmap)

    def _saveImage(self):
        ''' Function that saves image on users driver.
            Creates a folder named {keyword}_gallery in source directory.
        Then it saves currently displayed image in this folder.
        Names of saved images are just "img" with a number based on
        number of images in the folder.
        '''
        dir_name = self.ui.writeKeyword.text() + "_gallery"
        # checking if folder already exists, if not, creating a new folder
        if dir_name not in os.listdir('.'):
            os.mkdir(dir_name)
        # checking how many images are already in the folder
        img_count = len(os.listdir('.\\' + dir_name))
        image = self.ui._imgList[self.ui._displayedImg]
        image.PIL_image.save(f'.\\{dir_name}\\img{img_count + 1}.png')

    def _createCollage(self):
        ''' Function that creates and displayes collage of all 6 images.
        Any transformations made on pictures, such as rotation or filters, are
        saved and displayed on the collage.
            Collage is made out of 2 rows, 3 images each. Height of every
        image is set to 400 pixels. Horizontal distances between images are
        being split evenly.
        '''
        self.ui.stackedWidget.setCurrentIndex(2)
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
