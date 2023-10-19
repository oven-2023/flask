from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(255))
    nickname = Column(String(255))
    password = Column(String(255))

    def __init__(self, user_id, username, nickname, password):
        self.user_id = user_id
        self.username = username
        self.nickname = nickname
        self.password = password

class Work(Base):
    __tablename__ = 'work'

    work_id = Column(BigInteger, primary_key=True, autoincrement=True)
    title_kr = Column(String(255))
    title_eng = Column(String(255))
    year = Column(Integer)
    rating = Column(String(255))
    director = Column(String(255))
    actor = Column(String(255))
    summary = Column(String(10000))
    poster = Column(String(255))
    provider_list = relationship('WorkProvider', back_populates='work')

class WorkProvider(Base):
    __tablename__ = 'work_provider'

    work_provider_id = Column(BigInteger, primary_key=True, autoincrement=True)

    work_id = Column(BigInteger, ForeignKey('work.work_id'))
    work = relationship('Work', back_populates='provider_list')

    provider_id = Column(BigInteger, ForeignKey('provider.provider_id'))
    provider = relationship('Provider', back_populates='work_list')

class Provider(Base):
    __tablename__ = 'provider'

    provider_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))

    work_list = relationship('WorkProvider', back_populates='provider')


