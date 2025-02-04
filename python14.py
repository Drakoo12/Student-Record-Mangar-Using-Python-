import pickle
FILENAME = "students.pkl"

def save_records(records):
    with open(FILENAME, 'wb') as file:
        pickle.dump(records, file)

def load_records():
    with open(FILENAME, 'rb') as file:
        return pickle.load(file)

def append_record(roll_no, name, marks):
    records = load_records()
    records.append((roll_no, name, marks))
    save_records(records)

def update_marks(roll_no, new_marks):
    records = load_records()
    for i, record in enumerate(records):
        if record[0] == roll_no:
            records[i] = (roll_no, record[1], new_marks)
            save_records(records)
            return
    print(f"Record with roll number {roll_no} not found.")

def delete_record(roll_no):
    records = load_records()
    new_records = [record for record in records if record[0] != roll_no]
    save_records(new_records)

def display_records():
    records = load_records()
    for record in records:
        print(f"Roll No: {record[0]}, Name: {record[1]}, Marks: {record[2]}")

def search_record(roll_no):
    records = load_records()
    for record in records:
        if record[0] == roll_no:
            print(f"Roll No: {record[0]}, Name: {record[1]}, Marks: {record[2]}")
            return
    print(f"Record with roll number {roll_no} not found.")


try:
    load_records()
except (FileNotFoundError, EOFError):
    with open(FILENAME, 'wb') as file:
        pickle.dump([], file)

while True:
    print("\nChoose an operation:")
    print("1. Append Record")
    print("2. Update Marks")
    print("3. Delete Record")
    print("4. Display Records")
    print("5. Search Record")
    print("6. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        roll_no = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        append_record(roll_no, name, marks)
    elif choice == 2:
        roll_no = int(input("Enter roll number to update marks: "))
        new_marks = float(input("Enter new marks: "))
        update_marks(roll_no, new_marks)
    elif choice == 3:
        roll_no = int(input("Enter roll number to delete: "))
        delete_record(roll_no)
    elif choice == 4:
        display_records()
    elif choice == 5:
        roll_no = int(input("Enter roll number to search: "))
        search_record(roll_no)
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")