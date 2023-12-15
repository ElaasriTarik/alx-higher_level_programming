#!/usr/bin/python3
""" fetch all states """
import MySQLdb
import sys


def start(usr, password, database, search):
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        password=password,
        db=database
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE \
    name LIKE BINARY '{}' ORDER BY id".format(search))
    data = cur.fetchall()
    x = 1
    for row in data:
        print(row)


if __name__ == "__main__":
    username = sys.argv[1]
    passw = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    start(username, passw, database, search)
