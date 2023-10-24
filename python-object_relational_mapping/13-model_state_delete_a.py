#!/usr/bin/python3
# 13-model_state_delete_a.py
# Ethan Zalta
""" Removes states with the letter 'a'"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_a = session.query(State).filter(State.name.contains('a'))

    for state in states_a:
        session.delete(state)
    session.commit()
