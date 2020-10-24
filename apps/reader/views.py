from utils.genJsonResponse import json_response
from utils.ViewModel import BasicView
from apps.spider.models import SpiderData


class ReaderParamsView(BasicView):
    def __init__(self):
        super().__init__()

    def get(self, c_id):
        novel = self.session.query(SpiderData).filter_by(id=c_id).first()

        data = {
            'res': novel
        }
        return json_response(data=data)
