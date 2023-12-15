#!/usr/bin/python3
""" fetch all states """
import MySQLdb
import sys


def start(usr, password, database, keyword):
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        password=password,
        db=database
    )
    cur = con.cursor()
    query = "SELECT cities.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name LIKE %s \
    ORDER BY cities.id ASC"
    cur.execute(query, (keyword,))
    data = cur.fetchall()
    x = 1
    if data is not None:
        for row in data:
            print(row[0], end=", " if x < len(data) else "\n")
            x += 1


if __name__ == "__main__":
    username = sys.argv[1]
    passw = sys.argv[2]
    database = sys.argv[3]
    keyword = sys.argv[4]
    start(username, passw, database, keyword)
