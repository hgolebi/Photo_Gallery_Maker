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
        self.ui.enterButton.clicked.connect(lambda: self._search())


    def _search(self):
        pixmapa = QtGui.QPixmap()
        text = self.ui.writeKeyword.text()
        response = requests.get(url.format(KEYWORD=text))
        img_bytes = BytesIO(response.content)
        pixmapa.loadFromData(img_bytes.getvalue())
        self.ui.zdjecie.setPixmap(pixmapa)
        self.ui.stackedWidget.setCurrentIndex(1)


def guiMain(args):
    app = QtWidgets.QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()

if __name__ == "__main__":
    guiMain(sys.argv)