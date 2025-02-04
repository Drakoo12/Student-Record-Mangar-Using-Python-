import csv

FILENAME = "students.csv"

def create_csv():
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(("User ID", "Password")) 

def add_user(user_id, password):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, password])

def search_password(user_id):
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == user_id:
                return row[1]
    return None

create_csv()

while True:
    print("\nChoose an operation:")
    print("1. Add User")
    print("2. Search Password")
    print("3. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        user_id = input("Enter user ID: ")
        password = input("Enter password: ")
        add_user(user_id, password)
    elif choice == 2:
        user_id = input("Enter user ID to search: ")
        password = search_password(user_id)
        if password:
            print(f"Password for user ID {user_id} is {password}")
        else:
            print(f"User  ID {user_id} not found.")
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")