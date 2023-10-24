#!/usr/bin/python3
# 3-my_safe_filter_states.py
# Ethan Zalta
"""Lists all states where name matches input name, but safely"""
import MySQLdb
from sys import argv


def show_state_specific():
    """Shows all states that match with argv[4] input"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    c = db.cursor()

    state_name = argv[4]
    c.execute("SELECT * FROM states WHERE BINARY name = %(inputName)s"
              "ORDER BY id ASC", {'inputName': state_name})
    all_data = c.fetchall()

    for state in all_data:
        print(state)


if __name__ == "__main__":
    show_state_specific()
