#!/usr/bin/python3
# 1-filter_states.py
# Ethan Zalta
"""Lists all states where name starts with N"""
import MySQLdb
from sys import argv


def show_state_n():
    """Shows all states that begin with 'N'"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY id;")
    all_data = c.fetchall()

    for state in all_data:
        if state[1][0] == 'N':
            print(state)

    c.close()
    db.close()


if __name__ == "__main__":
    show_state_n()
