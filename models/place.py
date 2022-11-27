#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

place_amenity = Table('place_amenity', Base.metadata,
                Column('place_id', String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity", backref="places", viewonly=False)
        city_id = Column(String(60), ForeignKey('cities.id'))
        user_id = Column(String(60), ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Return all reviews for a place """
            return [Review.all(Review.place_id == self.id)]

        @property
        def amenities(self):
            """ Return all amenities for a place """
            return [Amenity.all(Amenity.id == self.id)]

        @amenities.setter
        def amenities(self, amenity_object):
            if type(amenity_object).__name__ == "Amenity":
                self.amenity_ids.append(amenity_object.id)
