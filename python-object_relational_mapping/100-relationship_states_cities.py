#!/usr/bin/python3
# 100-relationship_states_cities.py
# Ethan Zalta
""" List all states from database in order of id"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_city_state = City(name="San Francisco", state=State(name="California"))
    session.add(new_city_state)
    session.commit()
