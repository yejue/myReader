# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\reader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reader(object):
    def setupUi(self, reader):
        reader.setObjectName("reader")
        reader.resize(545, 369)
        self.horizontalLayout = QtWidgets.QHBoxLayout(reader)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tb_novels = QtWidgets.QTableWidget(reader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_novels.sizePolicy().hasHeightForWidth())
        self.tb_novels.setSizePolicy(sizePolicy)
        self.tb_novels.setMinimumSize(QtCore.QSize(113, 0))
        self.tb_novels.setMaximumSize(QtCore.QSize(113, 16777215))
        self.tb_novels.setObjectName("tb_novels")
        self.tb_novels.setColumnCount(2)
        self.tb_novels.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_novels.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_novels.setHorizontalHeaderItem(1, item)
        self.tb_novels.horizontalHeader().setStretchLastSection(True)
        self.tb_novels.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tb_novels)
        self.te_content = QtWidgets.QTextEdit(reader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_content.sizePolicy().hasHeightForWidth())
        self.te_content.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.te_content.setFont(font)
        self.te_content.setReadOnly(True)
        self.te_content.setProperty("markdown", "")
        self.te_content.setObjectName("te_content")
        self.horizontalLayout.addWidget(self.te_content)

        self.retranslateUi(reader)
        QtCore.QMetaObject.connectSlotsByName(reader)

    def retranslateUi(self, reader):
        _translate = QtCore.QCoreApplication.translate
        reader.setWindowTitle(_translate("reader", "Form"))
        item = self.tb_novels.horizontalHeaderItem(0)
        item.setText(_translate("reader", "id"))
        item = self.tb_novels.horizontalHeaderItem(1)
        item.setText(_translate("reader", "novel"))
        self.te_content.setHtml(_translate("reader", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
