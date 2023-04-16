#!/usr/bin/python3

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
