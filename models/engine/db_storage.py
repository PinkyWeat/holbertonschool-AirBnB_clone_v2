#!/usr/bin/python3
"""Database storage engine module"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """ Database storage engine module """
    __engine = None
    __session = None

    classes_list = {
        'User': User, 'Place': Place,
        'State': State, 'City': City,
        'Amenity': Amenity, 'Review': Review
    }

    def __init__(self):
        """ init function/constructor """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return all objects """
        values = dict()
        if cls is None:
            for clss in DBStorage.classes_list.values():
                for obj in self.__session.query(clss).all():
                    values[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for objct in self.__session.query(DBStorage.classes_list[cls]).all():
                values[objct.__class__.__name__ + '.' + objct.id] = objct
        return values

    def reload(self):
        """ Create all tables in current DB session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def new(self, obj):
        """ Adds an object """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """ Saves changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def close(self):
        """ Close method to call remove() method """
        self.__session.close()
