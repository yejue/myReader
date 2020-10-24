import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from apps.spider import views


class SpiderLoader:
    """
    爬虫数据loader，查、增
    """
    def __init__(self, frame, signals):
        # 传进来的窗口
        self.frame = frame
        self.signals = signals
        self.title = str
        self.content = str

    def post(self):
        """
        爬虫数据入库
        """
        data = {
            'title': self.title,
            'content': self.content
        }
        view = views.SpiderDataView()
        res = view.post(data)
        if res['errno'] != '0':
            return self.signals['err_signal'].emit(res['errmsg'])
        self.signals['load_signal'].emit('reader_loader')

    @staticmethod
    def get_novel(url):
        headers = {
            'User-Agent': UserAgent().Chrome
        }
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.content.decode('utf8'), 'html.parser')
        title = soup.find_all(class_='act')[0].getText()
        title2 = soup.find_all(class_='content-wrap')[0].getText()
        contents = soup.find_all('p')[6: -2]
        content = ''.join([i.getText() for i in contents])
        return title+title2, content

    def btn_clicked(self):
        """
        按钮被点击时的动作
        :return:
        """
        sender = self.frame.sender()
        if sender.objectName() == 'pushButton_find':
            return self.action_get()
        if sender.objectName() == 'pushButton_download':
            return self.action_download()

    def action_get(self):
        """
        数据爬取，返回状态到小说title， content 到te_status
        """
        url = self.frame.le_url.text()
        try:
            self.title, self.content = self.get_novel(url)
            self.frame.te_status.setPlainText(self.title + self.content)
        except Exception as e:
            self.signals['err_signal'].emit('{}'.format(e))

    def action_download(self):
        """
        下载入库
        """
        self.post()

