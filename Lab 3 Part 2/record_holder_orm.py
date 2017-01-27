from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base

from record_holder import RecordHolder

# Engine
engine = create_engine('sqlite:///records.db', echo=False)

Base
