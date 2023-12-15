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
    query = "SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id"
    cur.execute(query)
    data = cur.fetchall()
    x = 1
    for row in data:
        print(row)


if __name__ == "__main__":
    username = sys.argv[1]
    passw = sys.argv[2]
    database = sys.argv[3]
    start(username, passw, database)
