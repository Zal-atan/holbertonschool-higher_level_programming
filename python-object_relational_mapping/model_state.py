#!usr/bin/python3
# model_state.py
# Ethan Zalta
"""Class definition of a 'state', instantiates from Base = declarative_base"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class 'State' which will inherit behaviors from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
