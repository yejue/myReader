# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_myReader(object):
    def setupUi(self, myReader):
        myReader.setObjectName("myReader")
        myReader.resize(575, 356)
        self.gridLayout = QtWidgets.QGridLayout(myReader)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(myReader)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_spider = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_spider.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_spider.setObjectName("pushButton_spider")
        self.verticalLayout.addWidget(self.pushButton_spider)
        self.pushButton_reader = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_reader.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_reader.setObjectName("pushButton_reader")
        self.verticalLayout.addWidget(self.pushButton_reader)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.frame_content = QtWidgets.QFrame(myReader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy)
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.gridLayout.addWidget(self.frame_content, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(myReader)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setContentsMargins(0, 2, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_small = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_small.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_small.setMaximumSize(QtCore.QSize(31, 666))
        self.pushButton_small.setObjectName("pushButton_small")
        self.horizontalLayout.addWidget(self.pushButton_small)
        self.pushButton_close = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_close.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_close.setMaximumSize(QtCore.QSize(31, 666))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 2)

        self.retranslateUi(myReader)
        QtCore.QMetaObject.connectSlotsByName(myReader)

    def retranslateUi(self, myReader):
        _translate = QtCore.QCoreApplication.translate
        myReader.setWindowTitle(_translate("myReader", "MyReader"))
        self.pushButton_spider.setText(_translate("myReader", "爬行状态"))
        self.pushButton_reader.setText(_translate("myReader", "阅读器"))
        self.pushButton_small.setText(_translate("myReader", "-"))
        self.pushButton_close.setText(_translate("myReader", "×"))
