#!/usr/bin/python3
""" fetching all """
import sys
from model_state import Base, State
from sqlalchemy import create_engine, bindparam
from sqlalchemy.orm import sessionmaker


def start(username, password, database, search):
    engine = create_engine("mysql+mysqldb://{}:{}@localhost: \
    3306/{}".format(username, password, database), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State) \
                  .where(State.name.like("%"+bindparam("search")+"%")) \
                  .first()
    if data:
        print("{}".format(data.id))
    else:
        print("Not found")


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    start(username, password, database, search)