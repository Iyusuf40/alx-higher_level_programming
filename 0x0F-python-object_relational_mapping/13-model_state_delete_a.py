#!/usr/bin/python3
""" module contains sqlalchemy mapped table.
deletes some states row in states table"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def main():
    """main function"""
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    db_url = f"mysql+mysqldb://{user}:{pwd}@localhost/{db}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)  # redundant after first call
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))\
            .all()
    for state in states:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    main()
