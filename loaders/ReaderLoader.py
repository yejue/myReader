from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from apps.spider.views import SpiderDataView
from apps.reader.views import ReaderParamsView


class ReaderLoader:

    def __init__(self, frame, signals):
        self.frame = frame
        self.signals = signals

    def load(self):
        """
        加载当前所有的文章到列表
        """
        view = SpiderDataView()
        res = view.get()
        if res['data']:
            self.insert(res['data']['res'])

    def insert(self, data):
        row = len(data)
        self.frame.tb_novels.setRowCount(row)
        for r in range(row):
            item0 = QTableWidgetItem(str(data[r].id))
            item1 = QTableWidgetItem(str(data[r].title))

            self.frame.tb_novels.setItem(r, 0, item0)
            self.frame.tb_novels.setItem(r, 1, item1)


class ReaderParamsLoader:
    """
    加载novels 详细参数
    """
    def __init__(self, frame, signals):
        self.frame = frame
        self.signals = signals

    def load(self):
        c_id = self.current_id(self.frame.tb_novels)
        view = ReaderParamsView()
        res = view.get(c_id)
        if res['errno'] != '0':
            return self.signals['err_signal'].emit(res['errmsg'])
        self.insert(res['data']['res'])

    def insert(self, data):
        self.frame.te_content.setText(data.content)

    def current_id(self, tb: QTableWidget):
        row = tb.currentRow()
        c_id = tb.item(row, 0).text()
        return int(c_id)
