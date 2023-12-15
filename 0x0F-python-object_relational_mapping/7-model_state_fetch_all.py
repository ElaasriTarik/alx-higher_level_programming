#!/usr/bin/python3
""" fetching all """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def start(username, password, database):
    engine = create_engine("mysql+mysqldb://{}:{}@localhost: \
    3306/{}".format(username, password, database), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(State.id)

    for row in data:
        print(row.id, ":", row.name)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    start(username, password, database)
