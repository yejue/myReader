from PyQt5.QtWidgets import QWidget
from uis.spider import Ui_spider


class SpiderCtl(QWidget, Ui_spider):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
