#!/usr/bin/python3
# 0-select_states.py
# Ethan Zalta
""" This script lists all the states from database 'hbtn_0e_0_usa'
Inputs are mysql username, mysql password and database name"""

from MySQLdb import connect
from sys import argv


if __name__ == "__main__":
    """Shows all the states from the table in database"""
    # connect to database
    db = connect(host="localhost", port=3306, user=argv[1], passwd=argv[2],
                 database=argv[3])

    # cursor object
    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY id")
    all_data = c.fetchall()

    for row in all_data:
        print(row)

    c.close()  # close cursor
    db.close()  # close database connection
