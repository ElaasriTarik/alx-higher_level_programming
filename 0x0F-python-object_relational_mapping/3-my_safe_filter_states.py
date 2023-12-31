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
    query = "SELECT * FROM states WHERE \
    name LIKE BINARY %s ORDER BY id"
    cur.execute(query, (search,))
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
