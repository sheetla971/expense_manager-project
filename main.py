from sql import TripTable, UsersTable
def add_trip():
    trip_Name = input("Enter trip name:")
    trip_obj = TripTable(Name = trip_Name)
    trip_obj.insert()

def add_users():
    Name = input("Enter Name:")
    Email = input("Enter Email:")
    Phone = input("Enter Phone:")
    users_obj = UsersTable(Name = Name,Email = Email,Phone = Phone)
    users_obj.insert()

def expense_manager():
    print("1. Add Trip")
    print("2. Add Users")
    option_selected = int(input("Enter Option: "))
    print(option_selected)
    if option_selected == 1:
        add_trip()
    elif option_selected == 2:
        add_users()
    else:
        print("Invalid Action")

if __name__ == "__main__":
    print("WELCOME TO EXPENSE MANAGER PROJECT, TO START WITHSELECT GIVEN BELOW OPTIONS:")

    expense_manager()


