from sqlalchemy import Integer, Column, String, SmallInteger
# from flask import
from werkzeug.security import generate_password_hash,check_password_hash
from app.model.base import Base,db



class User(Base):

    id = Column(Integer,primary_key=True)
    email = Column(String(24),unique=True)
    nickname = Column(String(24),unique=True,nullable=False)
    auth = Column(SmallInteger,default=1)
    _password = Column('password',String(100))


    @property
    def password(self):

        return self._password

    @property
    def password(self,raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname,account,secret):

        with db.auto_commit():
            user = User()
            print('User register_by_email')
            user.nickname = nickname
            user.email = account
            user._password = secret
            db.session.add(user)


