from PyQt5.QtWidgets import QWidget
from uis.reader import Ui_reader


class ReaderCtl(QWidget, Ui_reader):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.change_ui()

    def change_ui(self):
        # 隐藏表格第0列
        self.tb_novels.setColumnHidden(0, True)
