# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\spider.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_spider(object):
    def setupUi(self, spider):
        spider.setObjectName("spider")
        spider.resize(443, 237)
        self.gridLayout = QtWidgets.QGridLayout(spider)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.te_status = QtWidgets.QPlainTextEdit(spider)
        self.te_status.setReadOnly(True)
        self.te_status.setObjectName("te_status")
        self.gridLayout.addWidget(self.te_status, 1, 0, 1, 1)
        self.le_url = QtWidgets.QLineEdit(spider)
        self.le_url.setMinimumSize(QtCore.QSize(30, 30))
        self.le_url.setObjectName("le_url")
        self.gridLayout.addWidget(self.le_url, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(spider)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_find = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_find.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_find.setObjectName("pushButton_find")
        self.horizontalLayout.addWidget(self.pushButton_find)
        self.pushButton_download = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_download.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout.addWidget(self.pushButton_download)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)

        self.retranslateUi(spider)
        QtCore.QMetaObject.connectSlotsByName(spider)

    def retranslateUi(self, spider):
        _translate = QtCore.QCoreApplication.translate
        spider.setWindowTitle(_translate("spider", "Form"))
        self.pushButton_find.setText(_translate("spider", "查找"))
        self.pushButton_download.setText(_translate("spider", "下载"))
