#!/usr/bin/python3
"""Database storage engine module"""
from os import getenv
from models.user import User
from models.base_model import BaseModel
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

classes = {"User": User,
         "City": City,
         "Amenity": Amenity,
         "State": State,
         "Review": Review,
         "Place": Place}

class DBStorage():
    """Database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Init function//constructor"""
        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}')
                        .format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                        getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                        pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.meta.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary with all values"""
        dc = {}
        if cls in classes.values() or cls is None:
            for key in self.__session.query(classes[cls.__class__.__name__]).all():
                dc[type(key).__name__+'.'+key.id] = key
        return dc

    def new(self, obj):
        """Add an object to the current database instance"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database instance"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the stated object if obj is not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Create all tables and creates the current database session"""
        Base.metadata.create_all(self.__engine)
        scop_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(scop_session)
        self.__session = Session
