from database_editor import DatabaseEditor

database = DatabaseEditor()

# Method to display the menu
def menu():
    print('''
    Chainsaw Juggling Record Menu:
    1. View all records.
    2. View individual record by name.
    3. Add record.
    4. Update record by name.
    5. Delete record by name.
    q. Quit
    ''')

def choice_handle():
    global database
    while True:
        menu()
        choice = input("Choose function: ")
        if choice == '1':
            database.get_all_records()
        elif choice == '2':
            name = input("Who would you like to search for? ")
            database.get_record(name)
        elif choice == '3':
            name = input("What is the record holders name: ")
            country = input("What is the country they belong to: ")
            while True:
                try:
                    catches = int(input("How many catches have they made: "))
                    break
                except ValueError:
                    print("Please enter a valid integer")
            database.add_record(name, country, catches)
        elif choice =='4':
            name = input("Who's record would you like to update? ")
            catches = input("How many catches have they made? ")
            database.update_record(name, catches)
        elif choice == '5':
            name = input("Who's record would you like to delete? ")
            database.delete_record(name)
        elif choice == 'q':
            break
        else:
            print("Please enter a valid choice.")

# Main function
def main():
    choice_handle()
    database.close()



main()
