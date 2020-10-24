from sqlalchemy import exists
from . import models
from utils import ViewModel
from utils.genJsonResponse import json_response
from utils.res_code import error_map, Code


class SpiderDataView(ViewModel.BasicView):
    """
    返回爬虫数据表数据
    """
    def get(self):
        """
        返回所有的小说数据
        """
        res = self.session.query(models.SpiderData).all()
        data = {
            'res': res
        }
        return json_response(data=data)

    def post(self, data):
        """
        存入数据库
        """
        # 查询是否存在
        if self.session.query(exists().where(models.SpiderData.title == data['title'])).scalar():
            return json_response(errno=Code.DATAEXIST, errmsg=error_map[Code.DATAEXIST])
        spi_data = models.SpiderData(title=data['title'], content=data['content'])

        try:
            self.session.add(spi_data)
            self.session.commit()
            return json_response(Code.OK)
        except Exception as e:
            return json_response(errno=Code.UNKOWNERR, errmsg='{}'.format(e))

