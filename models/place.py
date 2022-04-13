#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from models.engine.file_storage import FileStorage


fs = FileStorage()


class Place(BaseModel, Base):
    """ class represents Place object """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    """I have to find a way to do the following for DBStorage only"""
    reviews = relationship("Review", backref=place, cascade="all, delete")

    @property
    def reviews(self):
        """ getter method for reviews when place_id == Place.id"""
        reviews_list = []
        reviews = fs.all(Review)
        for review in reviews.values():
            if review.place_id == Place.id:
                reviews_list.append(review)
        return reviews_list
