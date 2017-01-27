from  database_editor import DatabaseEditor

database = DatabaseEditor()

database.initiate_database() # Initiate database

database.add_record('Anthony', 'United States', 0) # Addd test

print(database.get_record('Anthony'))

database.update_record('Anthony', 1) # Update test

print(database.get_record('Anthony'))

database.delete_record('Anthony')

print(database.get_record('Anthony'))
