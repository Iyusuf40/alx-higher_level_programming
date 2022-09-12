#!/usr/bin/python3
"""module contains City class that maps to cities
table in hbtn_0e_14_usa db"""


from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)
    state = relationship("State", backref="states")
