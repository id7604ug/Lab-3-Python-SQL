import sqlite3

db = sqlite3.connect('my_first_db.db') # Creates or opend database file

cur = db.cursor() # Need a cursor object to perform operations

# Create table
cur.execute('create table phones(brand text, version int)')

# Add some database
cur.execute('insert into phones values("Android", 5)')
cur.execute('insert into phones values("iPhone", 6)')

db.commit() # Save changes

# Execute a query
for row in cur.execute('select * from phones'):
    print(row)

cur.execute('drop table phones') # Delete table
db.commit()

db.close()
