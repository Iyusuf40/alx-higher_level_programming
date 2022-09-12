#!/usr/bin/python3
""" module contains sqlalchemy mapped table,
creates a new state row in states table"""


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
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == "__main__":
    main()
