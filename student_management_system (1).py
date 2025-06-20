students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    student = {"name": name, "roll": roll, "marks": marks}
    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\nStudent List:")
        for student in students:
            print(f"Name: {student['name']}, Roll No: {student['roll']}, Marks: {student['marks']}")

def search_student():
    roll = input("Enter roll number to search: ")
    for student in students:
        if student['roll'] == roll:
            print(f"Found: Name: {student['name']}, Marks: {student['marks']}")
            return
    print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("Student deleted.")
            return
    print("Student not found.")

def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
