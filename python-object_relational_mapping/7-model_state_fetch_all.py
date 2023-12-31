#!/usr/bin/python3
# 7-model_state_fetch_all.py
# Ethan Zalta
""" List all states from database in order of id"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id)

    for state in all_states:
        print(f"{state.id}: {state.name}")
