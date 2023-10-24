#!/usr/bin/python3
# 7-model_state_fetch_all.py
# Ethan Zalta
""" List all states from database in order of id"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def list_all_states():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id).all()

    for state in all_states:
        print(f"{state.id}: {state.name}")

if __name__ == "__main__":
    list_all_states()
