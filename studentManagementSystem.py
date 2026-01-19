# Student Record Management System

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\nStudent Records:")
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}")
    print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found: {s['name']} with Marks {s['marks']}\n")
            return
    print("Student not found.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
