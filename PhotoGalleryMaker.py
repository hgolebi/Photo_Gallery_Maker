# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PhotoGalleryMaker.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(815, 722)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackPage1 = QtWidgets.QWidget()
        self.stackPage1.setObjectName("stackPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.stackPage1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.galleryButton = QtWidgets.QPushButton(self.stackPage1)
        self.galleryButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.galleryButton.sizePolicy().hasHeightForWidth())
        self.galleryButton.setSizePolicy(sizePolicy)
        self.galleryButton.setMinimumSize(QtCore.QSize(60, 40))
        self.galleryButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.galleryButton.setObjectName("galleryButton")
        self.verticalLayout_2.addWidget(self.galleryButton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.appName = QtWidgets.QLabel(self.stackPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appName.sizePolicy().hasHeightForWidth())
        self.appName.setSizePolicy(sizePolicy)
        self.appName.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.appName.setBaseSize(QtCore.QSize(2000, 3000))
        self.appName.setObjectName("appName")
        self.verticalLayout_2.addWidget(self.appName)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.writeKeyword = QtWidgets.QLineEdit(self.stackPage1)
        self.writeKeyword.setObjectName("writeKeyword")
        self.horizontalLayout.addWidget(self.writeKeyword)
        self.enterButton = QtWidgets.QPushButton(self.stackPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enterButton.sizePolicy().hasHeightForWidth())
        self.enterButton.setSizePolicy(sizePolicy)
        self.enterButton.setMaximumSize(QtCore.QSize(100, 30))
        self.enterButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.enterButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.enterButton.setAutoDefault(False)
        self.enterButton.setDefault(False)
        self.enterButton.setFlat(False)
        self.enterButton.setObjectName("enterButton")
        self.horizontalLayout.addWidget(self.enterButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.wrongKeywordMessege = QtWidgets.QLabel(self.stackPage1)
        self.wrongKeywordMessege.setEnabled(False)
        self.wrongKeywordMessege.setObjectName("wrongKeywordMessege")
        self.verticalLayout_2.addWidget(self.wrongKeywordMessege)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.noteLabel = QtWidgets.QLabel(self.stackPage1)
        self.noteLabel.setObjectName("noteLabel")
        self.verticalLayout_2.addWidget(self.noteLabel)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.stackPage1)
        self.stackPage2 = QtWidgets.QWidget()
        self.stackPage2.setObjectName("stackPage2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.stackPage2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.waitingLabel = QtWidgets.QLabel(self.stackPage2)
        self.waitingLabel.setObjectName("waitingLabel")
        self.horizontalLayout_2.addWidget(self.waitingLabel)
        self.stackedWidget.addWidget(self.stackPage2)
        self.stackPage3 = QtWidgets.QWidget()
        self.stackPage3.setObjectName("stackPage3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.stackPage3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.backButton = QtWidgets.QPushButton(self.stackPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QtCore.QSize(60, 40))
        self.backButton.setObjectName("backButton")
        self.verticalLayout_10.addWidget(self.backButton, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.leftButton = QtWidgets.QPushButton(self.stackPage3)
        self.leftButton.setMaximumSize(QtCore.QSize(30, 100))
        self.leftButton.setObjectName("leftButton")
        self.horizontalLayout_6.addWidget(self.leftButton)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.rotLeftButton = QtWidgets.QPushButton(self.stackPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotLeftButton.sizePolicy().hasHeightForWidth())
        self.rotLeftButton.setSizePolicy(sizePolicy)
        self.rotLeftButton.setMaximumSize(QtCore.QSize(40, 40))
        self.rotLeftButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../icons/rotateleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotLeftButton.setIcon(icon)
        self.rotLeftButton.setObjectName("rotLeftButton")
        self.horizontalLayout_4.addWidget(self.rotLeftButton)
        self.rotRightButton = QtWidgets.QPushButton(self.stackPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotRightButton.sizePolicy().hasHeightForWidth())
        self.rotRightButton.setSizePolicy(sizePolicy)
        self.rotRightButton.setMinimumSize(QtCore.QSize(0, 40))
        self.rotRightButton.setMaximumSize(QtCore.QSize(40, 40))
        self.rotRightButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../../icons/rotateright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotRightButton.setIcon(icon1)
        self.rotRightButton.setObjectName("rotRightButton")
        self.horizontalLayout_4.addWidget(self.rotRightButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.blurredBox = QtWidgets.QCheckBox(self.stackPage3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.blurredBox.setFont(font)
        self.blurredBox.setObjectName("blurredBox")
        self.horizontalLayout_4.addWidget(self.blurredBox)
        self.black_whiteBox = QtWidgets.QCheckBox(self.stackPage3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.black_whiteBox.setFont(font)
        self.black_whiteBox.setObjectName("black_whiteBox")
        self.horizontalLayout_4.addWidget(self.black_whiteBox)
        self.saveButton = QtWidgets.QPushButton(self.stackPage3)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_4.addWidget(self.saveButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.imgStack = QtWidgets.QStackedWidget(self.stackPage3)
        self.imgStack.setObjectName("imgStack")
        self.img_page1 = QtWidgets.QWidget()
        self.img_page1.setObjectName("img_page1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.img_page1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img1 = QtWidgets.QLabel(self.img_page1)
        self.img1.setMaximumSize(QtCore.QSize(1920, 1080))
        self.img1.setScaledContents(False)
        self.img1.setAlignment(QtCore.Qt.AlignCenter)
        self.img1.setObjectName("img1")
        self.verticalLayout.addWidget(self.img1)
        self.imgStack.addWidget(self.img_page1)
        self.img_page2 = QtWidgets.QWidget()
        self.img_page2.setObjectName("img_page2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.img_page2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.img2 = QtWidgets.QLabel(self.img_page2)
        self.img2.setMaximumSize(QtCore.QSize(1920, 1080))
        self.img2.setScaledContents(False)
        self.img2.setAlignment(QtCore.Qt.AlignCenter)
        self.img2.setObjectName("img2")
        self.verticalLayout_3.addWidget(self.img2)
        self.imgStack.addWidget(self.img_page2)
        self.img_page3 = QtWidgets.QWidget()
        self.img_page3.setObjectName("img_page3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.img_page3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.img3 = QtWidgets.QLabel(self.img_page3)
        self.img3.setMaximumSize(QtCore.QSize(1920, 1080))
        self.img3.setScaledContents(False)
        self.img3.setAlignment(QtCore.Qt.AlignCenter)
        self.img3.setObjectName("img3")
        self.verticalLayout_4.addWidget(self.img3)
        self.imgStack.addWidget(self.img_page3)
        self.img_page4 = QtWidgets.QWidget()
        self.img_page4.setObjectName("img_page4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.img_page4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.img4 = QtWidgets.QLabel(self.img_page4)
        self.img4.setMaximumSize(QtCore.QSize(1920, 1080))
        self.img4.setScaledContents(False)
        self.img4.setAlignment(QtCore.Qt.AlignCenter)
        self.img4.setObjectName("img4")
        self.verticalLayout_5.addWidget(self.img4)
        self.imgStack.addWidget(self.img_page4)
        self.img_page5 = QtWidgets.QWidget()
        self.img_page5.setObjectName("img_page5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.img_page5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.img5 = QtWidgets.QLabel(self.img_page5)
        self.img5.setMaximumSize(QtCore.QSize(1920, 1000))
        self.img5.setScaledContents(False)
        self.img5.setAlignment(QtCore.Qt.AlignCenter)
        self.img5.setObjectName("img5")
        self.verticalLayout_6.addWidget(self.img5)
        self.imgStack.addWidget(self.img_page5)
        self.img_page6 = QtWidgets.QWidget()
        self.img_page6.setObjectName("img_page6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.img_page6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.img6 = QtWidgets.QLabel(self.img_page6)
        self.img6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img6.sizePolicy().hasHeightForWidth())
        self.img6.setSizePolicy(sizePolicy)
        self.img6.setMaximumSize(QtCore.QSize(1920, 1080))
        self.img6.setBaseSize(QtCore.QSize(1920, 1080))
        self.img6.setText("")
        self.img6.setScaledContents(False)
        self.img6.setAlignment(QtCore.Qt.AlignCenter)
        self.img6.setObjectName("img6")
        self.verticalLayout_7.addWidget(self.img6)
        self.imgStack.addWidget(self.img_page6)
        self.verticalLayout_8.addWidget(self.imgStack)
        self.collageButton = QtWidgets.QPushButton(self.stackPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collageButton.sizePolicy().hasHeightForWidth())
        self.collageButton.setSizePolicy(sizePolicy)
        self.collageButton.setMinimumSize(QtCore.QSize(200, 50))
        self.collageButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.collageButton.setObjectName("collageButton")
        self.verticalLayout_8.addWidget(self.collageButton, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.rightButton = QtWidgets.QPushButton(self.stackPage3)
        self.rightButton.setMaximumSize(QtCore.QSize(30, 100))
        self.rightButton.setObjectName("rightButton")
        self.horizontalLayout_6.addWidget(self.rightButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.stackedWidget.addWidget(self.stackPage3)
        self.stackPage4 = QtWidgets.QWidget()
        self.stackPage4.setObjectName("stackPage4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.stackPage4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.returnButton = QtWidgets.QPushButton(self.stackPage4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnButton.sizePolicy().hasHeightForWidth())
        self.returnButton.setSizePolicy(sizePolicy)
        self.returnButton.setMinimumSize(QtCore.QSize(60, 40))
        self.returnButton.setObjectName("returnButton")
        self.horizontalLayout_8.addWidget(self.returnButton, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.collageImg1 = QtWidgets.QLabel(self.stackPage4)
        self.collageImg1.setObjectName("collageImg1")
        self.horizontalLayout_5.addWidget(self.collageImg1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.collageImg2 = QtWidgets.QLabel(self.stackPage4)
        self.collageImg2.setObjectName("collageImg2")
        self.horizontalLayout_5.addWidget(self.collageImg2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.collageImg3 = QtWidgets.QLabel(self.stackPage4)
        self.collageImg3.setObjectName("collageImg3")
        self.horizontalLayout_5.addWidget(self.collageImg3)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.collageImg4 = QtWidgets.QLabel(self.stackPage4)
        self.collageImg4.setObjectName("collageImg4")
        self.horizontalLayout_7.addWidget(self.collageImg4)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.collageImg5 = QtWidgets.QLabel(self.stackPage4)
        self.collageImg5.setObjectName("collageImg5")
        self.horizontalLayout_7.addWidget(self.collageImg5)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.collageImg6 = QtWidgets.QLabel(self.stackPage4)
        self.collageImg6.setObjectName("collageImg6")
        self.horizontalLayout_7.addWidget(self.collageImg6)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem18)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem19)
        self.stackedWidget.addWidget(self.stackPage4)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.imgStack.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PhotoGallery Maker"))
        self.galleryButton.setText(_translate("MainWindow", "To Gallery"))
        self.appName.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Welcome to </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">PHOTOGALLERY MAKER</span></p></body></html>"))
        self.writeKeyword.setPlaceholderText(_translate("MainWindow", "Type what do you want to see"))
        self.enterButton.setText(_translate("MainWindow", "Enter"))
        self.wrongKeywordMessege.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#d12646;\">Couldn\'t find any photo. Try different keyword.</span></p></body></html>"))
        self.noteLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Notice: Searching process may take up to 15 seconds </p></body></html>"))
        self.waitingLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Your photogallery is being created using Unsplash API</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:24pt;\">This may take a while..</span></p></body></html>"))
        self.backButton.setText(_translate("MainWindow", "Go Back"))
        self.leftButton.setText(_translate("MainWindow", "<"))
        self.blurredBox.setText(_translate("MainWindow", "blurred"))
        self.black_whiteBox.setText(_translate("MainWindow", "black and white"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.img1.setText(_translate("MainWindow", "TextLabel"))
        self.img2.setText(_translate("MainWindow", "TextLabel"))
        self.img3.setText(_translate("MainWindow", "TextLabel"))
        self.img4.setText(_translate("MainWindow", "TextLabel"))
        self.img5.setText(_translate("MainWindow", "TextLabel"))
        self.collageButton.setText(_translate("MainWindow", "Create collage"))
        self.rightButton.setText(_translate("MainWindow", ">"))
        self.returnButton.setText(_translate("MainWindow", "Go Back"))
        self.collageImg1.setText(_translate("MainWindow", "TextLabel"))
        self.collageImg2.setText(_translate("MainWindow", "TextLabel"))
        self.collageImg3.setText(_translate("MainWindow", "TextLabel"))
        self.collageImg4.setText(_translate("MainWindow", "TextLabel"))
        self.collageImg5.setText(_translate("MainWindow", "TextLabel"))
        self.collageImg6.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
