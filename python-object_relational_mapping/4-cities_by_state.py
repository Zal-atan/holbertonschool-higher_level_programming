#!/usr/bin/python3
# 4-cities_by_state.py
# Ethan Zalta
"""Lists all cities in order of id and their attached state"""
import MySQLdb
from sys import argv


def show_city_state():
    """Shows all cities in order of id and the state attatched"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    c = db.cursor()

    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
              INNER JOIN states ON states.id = cities.state_id\
              ORDER BY id ASC;")
    all_data = c.fetchall()

    for state in all_data:
        print(state)

    c.close()
    db.close()


if __name__ == "__main__":
    show_city_state()
