#!/usr/bin/python3
# 7-model_state_fetch_all.py
# Ethan Zalta
""" List all states from database in order of id"""
import sys
from model_state import Base, State
from sqlalchemy import sessionmaker
from sqlalchemy import (create_engine)

def all_states():
    engine = create_engine()
