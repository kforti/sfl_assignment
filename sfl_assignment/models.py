from dataclasses import dataclass
from typing import Dict

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


@dataclass
class Configuration:
    environment: str
    data_access: Dict
    database: Dict


class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     first_name = Column(String)
     last_name = Column(String)
     email = Column(String)
     gender = Column(String)
     ip_address = Column(String)


class UserSerializer:
    def serialize(self, user):
        return vars(user)

    def deserialize(self, data):
        user = User(
            id=data.get('id'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            gender=data.get('gender'),
            ip_address=data.get('ip_address')
        )
        return user


class UserRepository:
    serializer = UserSerializer()

    def __init__(self, session):
        self.session = session

    def add(self, data):
        person = self.serializer.deserialize(data)
        self.session.add(person)
