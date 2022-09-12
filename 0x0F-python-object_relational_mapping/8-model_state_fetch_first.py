#!/usr/bin/python3
""" module contains sqlalchemy usage code
for querying database"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """program entry"""
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    db_url = f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    obj = session.query(State).first()
    return obj


if __name__ == "__main__":
    obj = main()
    if (obj):
        print(str(obj.id) + ":", obj.name)
