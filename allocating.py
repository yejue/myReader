import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import pyqtSignal
from main_controller import MainController

from loaders.SpiderLoader import SpiderLoader
from loaders.ReaderLoader import ReaderLoader, ReaderParamsLoader


class AllocatingCenter(MainController):
    """
    分拨中心
    """
    # 实例化两个信号，一个加载页面，一个传递错误
    load_signal = pyqtSignal(str)
    err_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # 信号s
        self.signals = {
            'load_signal': self.load_signal,
            'err_signal': self.err_signal,
        }
        # 信号连接动作
        self.load_signal.connect(self.load_one)
        self.err_signal.connect(self.err_raise)
        # 爬虫页面，下发页面和信号
        self.spi_loader = SpiderLoader(self.spider, self.signals)
        # 阅读器页面
        self.reader_loader = ReaderLoader(self.reader, self.signals)
        self.read_params = ReaderParamsLoader(self.reader, self.signals)
        # 需要自动加载的页面
        self.loadNeeding = [self.reader_loader]
        self.load_all()
        # 一些操作集
        self.action_all()

    def load_one(self, load_name):
        """ load 单一页面 """
        self.__dict__[load_name].load()

    def load_all(self):
        for loader in self.loadNeeding:
            loader.load()

    def err_raise(self, err):
        """ 抛出某个错误提示 """
        return QMessageBox.critical(self, '错误', '{}'.format(err), QMessageBox.Yes)

    def action_all(self):
        self.action_spider()
        self.action_reader()

    def action_spider(self):
        # 点击查找，查找
        self.spider.pushButton_find.clicked.connect(self.spi_loader.btn_clicked)
        # 点击下载，入库
        self.spider.pushButton_download.clicked.connect(self.spi_loader.btn_clicked)

    def action_reader(self):
        # 点击加载
        self.reader.tb_novels.itemSelectionChanged.connect(self.read_params.load)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AllocatingCenter()
    win.show()
    sys.exit(app.exec_())
