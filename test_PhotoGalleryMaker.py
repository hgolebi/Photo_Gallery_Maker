from PhotoGalleryMaker import MainWindow
from PyQt5 import QtWidgets
import sys

url = 'https://source.unsplash.com/featured/?{KEYWORD}'
app = QtWidgets.QApplication(sys.argv)
mw = MainWindow()

def test_search():
    mw._search()
    assert mw.ui.stackedWidget.currentIndex() == 1
    assert mw.ui._currentImageIndex == 0
    assert mw.ui.imgStack.currentIndex() == 0
    assert mw.ui.galleryButton.isEnabled()

def test_swipeLeft_swipeRight():
    mw._search()
    mw.ui.imgStack.setCurrentIndex(2)
    mw.ui._currentImageIndex = 2
    mw._swipeLeft()
    assert mw.ui.imgStack.currentIndex() == 1
    assert mw.ui._currentImageIndex == 1
    mw._swipeRight()
    assert mw.ui.imgStack.currentIndex() == 2
    assert mw.ui._currentImageIndex == 2


def test_swipeLeft_first_photo():
    mw._search()
    mw.ui.imgStack.setCurrentIndex(0)
    mw.ui._currentImageIndex = 0
    mw._swipeLeft()
    assert mw.ui.imgStack.currentIndex() == 0
    assert mw.ui._currentImageIndex == 0


def test_swipeRight_last_photo():
    mw._search()
    mw.ui.imgStack.setCurrentIndex(5)
    mw.ui._currentImageIndex = 5
    mw._swipeRight()
    assert mw.ui.imgStack.currentIndex() == 5
    assert mw.ui._currentImageIndex == 5


def test_rotate_left():
    mw._search()
    image = mw.ui._imgList[mw.ui._currentImageIndex]
    image_height = image.pixmap().height()
    image_width = image.pixmap().width()
    image_ratio = image_height/image_width
    assert image.angle == 0
    mw._rotate('L')
    assert image.angle == 90
    new_image_ratio = image.pixmap().height()/image.pixmap().width()
    assert round(new_image_ratio, 2) == round(1/image_ratio, 2)
    mw._rotate('L')
    assert image.angle == 180
    new_image_ratio = image.pixmap().height()/image.pixmap().width()
    assert new_image_ratio == image_ratio


def test_rotate_right():
    mw._search()
    image = mw.ui._imgList[mw.ui._currentImageIndex]
    image_height = image.pixmap().height()
    image_width = image.pixmap().width()
    image_ratio = image_height/image_width
    assert image.angle == 0
    mw._rotate('R')
    assert image.angle == -90
    new_image_ratio = image.pixmap().height()/image.pixmap().width()
    assert round(new_image_ratio, 2) == round(1/image_ratio, 2)
    mw._rotate('R')
    assert image.angle == -180
    new_image_ratio = image.pixmap().height()/image.pixmap().width()
    assert new_image_ratio == image_ratio


def test_create_collage():
    mw._search()
    mw._createCollage()
    assert mw.isFullScreen()
    assert mw.ui.stackedWidget.currentIndex() == 2