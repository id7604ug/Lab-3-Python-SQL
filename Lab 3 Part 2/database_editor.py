import sqlite3

class DatabaseEditor:
    records = []
    db = sqlite3.connect('juggling_records.db') # Creates and opend the database
    cur = db.cursor() # Cursot to perform operations

    def initiate_database(self): # Create initial table
        self.cur.execute('CREATE table IF NOT EXISTS JugglingRecords (name text, country text, catches int)')
        self.db.commit() # Save

    def load_data(self): # Might not be necessary
        # Iterate over each row in the db
        for row in self.cur.execute('SELECT * from jugglingrecords'):
            records.append(row)

    def add_record(self, name, country, catches):
        # Execute parameterised insert statement
        self.cur.execute('INSERT into jugglingrecords values (?, ?, ?)', (name, country, catches))
        self.db.commit() # Commit insert
        print("Record inserted") # Test

    def delete_record(self, name): # Method to delete a record by name
        # Execute parameterised delete statement
        self.cur.execute('DELETE from jugglingrecords WHERE name = ?', (name, ))
        print("Record deleted.") # Test
        self.db.commit()

    def get_record(self, name): # Method to retrieve records by name
        records = self.cur.execute('SELECT * FROM jugglingrecords')
        for row in records:
            if row[0] == name:
                record = row
        return format_record(record)


    def get_all_records(self): # Method to get all records
        records = []
        print("Here is each record stored:")
        data = self.cur.execute('SELECT * FROM jugglingrecords')
        for row in data:
            records.append(self.format_record(row))
        for juggling_record in records:
            print(juggling_record)

    def format_record(self, record): # Method to format the given record as a string
        # Format return string
        record_string = "Record Holder: " + str(record[0]) + " Country: " + str(record[1]) + " Catches: " + str(record[2])
        return record_string

    def update_record(self, name, catches): # Method to update a record by name
        self.cur.execute('UPDATE jugglingrecords SET catches = ? WHERE name = ?', (catches, name))
        self.db.commit()
        print("Record updated.")

    def close(self): # Method to save database stuff
        self.cur.close()
