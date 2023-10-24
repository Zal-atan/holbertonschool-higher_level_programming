#!/usr/bin/python3
# relationship_city.py
# Ethan Zalta
"""Class definition of a 'state', instantiates from Base = declarative_base"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class 'City' which will inherit behaviors from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable = False)
