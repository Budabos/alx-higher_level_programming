#!/usr/bin/python3
"""script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
    Usage: ./0-select_states.py <mysql username>\
 <mysql password> <database name>\
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    search = sys.argv[4]
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY id ASC".format(search)
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)
