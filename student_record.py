import json

students = []

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")

    student = {
        "name": name,
        "roll": roll
    }

    students.append(student)
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No Records Found")
    else:
        for student in students:
            print(student)

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)
    print("Data Saved")

while True:
    print("\nStudent Record Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save Data")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        save_data()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")