#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel):
    """ State class """
    name = "" """Column(String(128), nullable=False)
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    else:

        @property
        def cities(self):
            from models import storage
            lst = []
            for val in storage.all(City).values():
                if self.id == val.state_id:
                    lst.append(val)
            return lst """
