#!/usr/bin/python3
"""practice module"""


from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """main function"""
    ls = sys.argv[1:]
    user = ls[0]
    pwd = ls[1]
    db = ls[2]
    db_url = f"mysql+mysqldb://{user}:{pwd}@localhost/{db}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
    session.close()


if __name__ == "__main__":
    main()
