#!/usr/bin/python3
""" fetch all states """


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
    for row in data:
        print(row)

if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    passw = sys.argv[2]
    database = sys.argv[3]
    start(username, passw, database)
