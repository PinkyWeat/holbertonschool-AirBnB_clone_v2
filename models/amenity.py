#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """ Amenity class for HBNB project """
    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        name = ""
