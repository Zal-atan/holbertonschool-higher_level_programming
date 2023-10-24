#!/usr/bin/python3
# 14-model_city_fetch_by_state.py
# Ethan Zalta
"""Prints all cities and which states they are from """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
        .filter(City.state_id == State.id).order_by(City.id):

        print(f"{state.name}: ({city.id}) {city.name}")
