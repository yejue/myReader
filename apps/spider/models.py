# coding: utf-8
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class SpiderData(Base):
    __tablename__ = 'spider_data'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    content = Column(Text)
