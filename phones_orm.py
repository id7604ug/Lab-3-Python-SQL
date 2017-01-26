from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3, phone
from phone import Phone

# Engine represents the core interface to the database
# The first argument is the url of the database;
# this points to a sqlitedb saved in a file called phone.db
# echo=True turns on (lots of!) logging
engine = create_engine('sqlite:///phone.db', echo=True)

Base = phone.Base # All of the mapped classes inherit from this class.

Base.metadata.create_all(engine) # Create a table for all the classes that use Base

# Create phone object
phone = Phone(brand='Samsung', version=6)

# Need a Session to talk to the database.
# A session manages mappings of objects to rows in the database.
# Make a Session class. Only need to do this one time.
Session = sessionmaker(bind=engine)   #Use the engine created earlier

# Ask the Session to instantiate a session object.
# We'll use the session object to talk to the DB
save_session = Session()

# Add the phone object to the session. This tells the session that we want
# to map the phone object to a row in the database
save_session.add(phone)
# The phone is pending - not yet saved. It won't be saved to the DB until the session is committed, or closed

# Commit to save changes
save_session.commit()  # now phone should be saved in DB

# Add more phones

phone2 = Phone(brand='iPhone', version=6)
phone3 = Phone(brand='Nokia', version=3)
phone4 = Phone(brand='Motorola', version=4)

# Can add a list of phones
save_session.add_all([ phone2, phone3, phone4 ])

# Can modify data in any of the added phones. Don't need to add again
phone2.brand = 'Apple' #change attribute of one object
phone4.version = 10 #change attribute of another object

save_session.commit()   # All phones saved

# Done? Close session. The phone objects are disconnected from the DB
# So close session when done; or if you need to use the objects again,
# add them to an open session.
save_session.close()

search_session = Session()

# Fetch everything.
# Query returns an Query object, which can be looped over
# producing  Phone objects

for phone in search_session.query(Phone):
    print(phone)

# Get a list of phone objects
all_phones_list = search_session.query(Phone).all()

# Fetch first phone in the results. This returns a Phone object
print(search_session.query(Phone).first())

# Filter - all phones with version greater than 4
results = search_session.query(Phone).filter(Phone.version > 4).all()

# More filtering
# Match phones where version is greater than 4, order by brand
for phone in search_session.query(Phone).filter(Phone.version > 4).order_by(Phone.brand):
    print(phone)

# Matching with like, call a function. Match all phones with 'o' in the brand
for phone in search_session.query(Phone).filter(Phone.brand.like('%s%')):
    print(phone)

# filter_by method is for simpler queries
print(search_session.query(Phone).filter_by(id=4))
print(search_session.query(Phone).filter_by(brand='Nokia'))


# Expect exactly one result? use one() which will return an object;
# or an error if there are 0 or 2+ items
# There's also a method one_or_none() which returns None if no item found.
print(search_session.query(Phone).filter_by(id=4).one())
# Useful for filtering with primary keys, where exactly one result is expected
