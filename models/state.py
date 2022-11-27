#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City

class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """ Getter method """
            from models import storage
            stlst = []
            list_obj = models.storage.all(City)
            for city in list_obj.values():
                if city.state_id == self.id:
                    stlst.append(city)
            return stlst
