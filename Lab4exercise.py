# student_management.py

# Initialize the data structures
students_list = []
students_dict = {}

def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")

    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}

    print(f"Student {name} added successfully!")
    print_student_details()

def print_student_details():
    print("Current student details:")
    for name, details in students_dict.items():
        print(f"Name: {name}, Age: {details['age']}, Grade: {details['grade']}")

def search_student():
    name = input("Enter student's name to search: ")
    if name in students_dict:
        details = students_dict[name]
        print(f"Student found - Name: {name}, Age: {details['age']}, Grade: {details['grade']}")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student's name to remove: ")
    if name in students_dict:
        students_list.remove(name)
        del students_dict[name]
        print(f"Student {name} removed successfully!")
    else:
        print("Student not found.")
    print_student_details()

def main():
    while True:
        print("\nStudent Information Management System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Remove Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
