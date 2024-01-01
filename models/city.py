#!/usr/bin/python3
""" Defines City Class and its attributes """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage_type

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if storage_type == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        state_id = ''
        name = ''


    def __init__(self, *args, **kwargs):
        """ initializes city """
        super().__init__(*args, **kwargs)
