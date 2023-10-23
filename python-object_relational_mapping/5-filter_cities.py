#!/usr/bin/python3
# 5-filter_cities.py
# Ethan Zalta
"""Search a state to see all cities associated in table"""
import MySQLdb
from sys import argv


def show_city_state():
    """Search a state as argv4 to see all cities associated"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    c = db.cursor()

    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
              INNER JOIN states ON states.id = cities.state_id\
              WHERE states.name = %(input_state)s\
              ORDER BY id ASC;", {"input_state": argv[4]})
    all_data = c.fetchall()

    num_cities = len(all_data)
    if num_cities == 0:
        print()
        return

    for i in range(0, num_cities - 1):
        print(all_data[i][1], end=", ")
    print(all_data[num_cities - 1][1])

    c.close()
    db.close()


if __name__ == "__main__":
    show_city_state()
