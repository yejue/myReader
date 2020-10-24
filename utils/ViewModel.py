from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BasicView:
    def __init__(self):
        self.session = self.db_connect('myreader.db')

    def db_connect(self, db):
        # 创建一个引擎
        engine = create_engine('sqlite:///{}?check_name_thread=False'.format(db), echo=False)
        # 创建一个会话
        Session = sessionmaker(bind=engine)
        session = Session()

        return session
