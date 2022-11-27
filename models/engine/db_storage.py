#!/usr/bin/python3
"""Database storage engine module"""
from models.user import User
from models.base_model import BaseModel
from models.base_model import Base
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class DBStorage():
    """Database"""
    __engine = None
    __session = None
    classes = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def __init__(self):
        """inisialization"""
        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}')
                                        .format(getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """all func"""
        values = dict()
        if cls is None:
            for clss in DBStorage.classes.values():
                for obj in self.__session.query(clss).all():
                    values[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for obj in self.__session.query(DBStorage.classes[cls]).all():
                values[obj.__class__.__name__ + '.' + obj.id] = obj
        return values

    def new(self, obj):
        """new"""
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj == None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """close"""
        self.__session.close()
