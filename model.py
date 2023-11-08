import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    user_id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String(255))
    nickname = sqlalchemy.Column(sqlalchemy.String(255))
    password = sqlalchemy.Column(sqlalchemy.String(255))

    def __init__(self, user_id, username, nickname, password):
        self.user_id = user_id
        self.username = username
        self.nickname = nickname
        self.password = password


class Work(Base):
    __tablename__ = 'work'

    work_id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    title_kr = sqlalchemy.Column(sqlalchemy.String(255))
    title_eng = sqlalchemy.Column(sqlalchemy.String(255))
    year = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.String(255))
    director = sqlalchemy.Column(sqlalchemy.String(255))
    actor = sqlalchemy.Column(sqlalchemy.String(255))
    summary = sqlalchemy.Column(sqlalchemy.String(10000))
    poster = sqlalchemy.Column(sqlalchemy.String(255))
    provider_list = relationship('WorkProvider', back_populates='work')

    action = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    sf = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    fantasy = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    adventure = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    criminal = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    thriller = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    mystery = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    comedy = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    romance = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    drama = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    animation = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    horror = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    variety = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    documentary = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    musical = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    family = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    western = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    war = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    performance = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    adult = sqlalchemy.Column(sqlalchemy.Integer, default=False)
    music = sqlalchemy.Column(sqlalchemy.Integer, default=False)

class WorkProvider(Base):
    __tablename__ = 'work_provider'

    work_provider_id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)

    work_id = sqlalchemy.Column(sqlalchemy.BigInteger, sqlalchemy.ForeignKey('work.work_id'))
    work = relationship('Work', back_populates='provider_list')

    provider_id = sqlalchemy.Column(sqlalchemy.BigInteger, sqlalchemy.ForeignKey('provider.provider_id'))
    provider = relationship('Provider', back_populates='work_list')

class Provider(Base):
    __tablename__ = 'provider'

    provider_id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(255))

    work_list = relationship('WorkProvider', back_populates='provider')

class RatingWork(Base):
    __tablename__ = 'rating_work'

    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)

    user_id = sqlalchemy.Column(sqlalchemy.BigInteger, sqlalchemy.ForeignKey('user.user_id'))
    work_id = sqlalchemy.Column(sqlalchemy.BigInteger, sqlalchemy.ForeignKey('work.work_id'))

    rating = sqlalchemy.Column(sqlalchemy.Float)