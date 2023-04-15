#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    mysql_user = sys.argv[1]
    mysql.pwd = sys.argv[2]
    db_name = sys.argv[2]

    db = MySQLdb.connect(
        host = 'localhost',
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3],
        port = 3306,
    )

    cursor = db.cursor()

    cursor.execute("SELECT *FROM states ORDER BY states.id ASC")

    raws = cursor.fetchall()

    for row in raws:
        print(row)

        cursor.close()
        db.close()
