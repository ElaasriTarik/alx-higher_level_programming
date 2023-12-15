#!/usr/bin/python3
""" fetch all states """
import MySQLdb
import sys


def start(usr, password, database):
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        password=password,
        db=database
    )
    cur = con.cursor()
    cur.execute("SELECT name FROM states ORDER BY id")
    data = cur.fetchall()
    x = 1
    for row in data:
        if x < 6:
            print("({}, '{}')".format(x, row[0]))
            x += 1


if __name__ == "__main__":
    username = sys.argv[1]
    passw = sys.argv[2]
    database = sys.argv[3]
    start(username, passw, database)
