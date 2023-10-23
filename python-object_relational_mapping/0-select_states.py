#!/usr/bin/python3
""" This script lists all the states from database 'hbtn_0e_0_usa'
Inputs are mysql username, mysql password and database name"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])
    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY id ASC")
    all_data = c.fetchall()

    for row in all_data:
        print(row)
