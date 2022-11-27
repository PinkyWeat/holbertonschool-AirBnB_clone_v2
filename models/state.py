#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    elif getenv("HBNB_TYPE_STORAGE") == "file":

        @property
        def cities(self):
            """ Return all cities from the current state instance """
            from models import storage
            lst = []
            for k, v in storage.all(City):
                if self.id == v.state.id:
                    lst.append(v)
            return lst
