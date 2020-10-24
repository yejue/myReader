import sys
from PyQt5.QtWidgets import QWidget, QApplication, QStackedLayout
from PyQt5.QtCore import Qt

from uis.main import Ui_myReader
from templates.basic_frame import MainPage
from controllers.ReaderCtl import ReaderCtl
from controllers.SpiderCtl import SpiderCtl


class MainController(MainPage, Ui_myReader):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 实例化子窗口
        self.reader = ReaderCtl()
        self.spider = SpiderCtl()
        # 设置堆叠布局
        self.qsl = QStackedLayout(self.frame_content)
        self.qsl.addWidget(self.spider)
        self.qsl.addWidget(self.reader)
        # 更改ui
        self.change_ui()
        # 加载qss
        self.setStyleSheet(self.load_style('main.qss'))
        # 槽函数绑定
        self.bind_slot()

    def bind_slot(self):
        """
        绑定槽函数
        """
        self.pushButton_spider.clicked.connect(self.switch)
        self.pushButton_reader.clicked.connect(self.switch)

    def switch(self):
        """
        菜单栏切换
        """
        sender = self.sender()

        index = {
            "pushButton_spider": 0,
            "pushButton_reader": 1,
        }
        self.qsl.setCurrentIndex(index[sender.objectName()])

    def change_ui(self):
        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 阴影
        eff_shadow = self.setShadow((0, 105, 157), r=1)
        self.pushButton_spider.setGraphicsEffect(eff_shadow)
        # 圆角
        self.setCircle(self)

