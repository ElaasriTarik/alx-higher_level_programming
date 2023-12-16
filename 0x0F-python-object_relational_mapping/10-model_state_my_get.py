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
                  .where(State.name == search) \
                  .first()
    if data is None:
        print("Not found")
    else:
        print("{}".format(data.id))


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    start(username, password, database, search)
