from . import models
from utils import ViewModel


class SpiderDataView(ViewModel.BasicView):
    """
    返回爬虫数据表数据
    """
    def get(self):
        pass

    def post(self, data):
        """
        存入数据库
        """
        pass
