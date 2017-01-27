from sqlalchemy import Column, Integer, string
from base import base

class RecordHolder(Base)

    # Add a table name
    __tablename__ = 'jugglingrecords'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    catches = Column(Integer)

    __init__(self, name, country, catches):
