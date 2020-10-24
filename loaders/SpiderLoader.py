import requests
from bs4 import BeautifulSoup

from apps.spider import view

class SpiderParams:
    """
    爬虫数据loader，查、增
    """
    def __init__(self, frame):
        # 传进来的窗口
        self.frame = frame

    def post(self):
        """
        爬虫数据入库
        """
        pass

    def get_novel(self):
        """
        返回爬到的一丢丢小说
        """
        pass

    def btn_clicked(self):
        """
        按钮被点击时的动作
        :return:
        """
        sender = self.