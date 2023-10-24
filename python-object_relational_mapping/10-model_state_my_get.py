#!/usr/bin/python3
# 10-model_state_my_get.py
# Ethan Zalta
""" Search database for a specific state"""
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

    all_states = session.query(State).order_by(State.id)

    search_state = argv[4]

    flag = 0
    for state in all_states:
        if search_state == state.name:
            print(f"{state.id}")
            flag += 1

    if flag == 0:
        print("Not found")
