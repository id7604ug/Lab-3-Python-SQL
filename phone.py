from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Phone(Base):

    # At the minimum, need a table name
    __tablename__ = 'phones'

    # And at least one column.
    # Create three columns: id, brand, version.
    # These attributes will be the column names, and the have the types specified.
    id = Column(Integer, primary_key=True)
    brand = Column(String)
    version = Column(Integer)

    def __repr__(self): # Returns a string representation of the object
        return 'Phone: id = {} brand = {} version = {}'.format(self.id, self.brand, self.version)
