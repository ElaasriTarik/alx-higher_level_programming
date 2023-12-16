#!/usr/bin/python3
""" fetching all """
import sys
from model_state import Base, State
from sqlalchemy import create_engine, bindparam
from sqlalchemy.orm import sessionmaker


def start(username, password, database):
    engine = create_engine("mysql+mysqldb://{}:{}@localhost: \
    3306/{}".format(username, password, database), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    to_delete = session.query(State).where(State.name.like("%a%")) \
                                    .order_by(State.id)
    for st in to_delete:
        session.delete(st)
    session.commit()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    start(username, password, database)
