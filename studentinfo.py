class StudentManagementSystem:
    def __init__(self):
        self.students_list = []  # List to store student names
        self.students_dict = {}  # Dictionary to store student info (name -> (age, grade))

    def add_student(self, name, age, grade):
        self.students_list.append(name)
        self.students_dict[name] = (age, grade)

    def search_student(self, name):
        if name in self.students_dict:
            age, grade = self.students_dict[name]
            print(f"Student found! Name: {name}, Age: {age}, Grade: {grade}")
        else:
            print(f"Student '{name}' not found.")

    def remove_student(self, name):
        if name in self.students_dict:
            del self.students_dict[name]
            self.students_list.remove(name)
            print(f"Student '{name}' removed successfully.")
        else:
            print(f"Student '{name}' not found.")

    def display_all_students(self):
        print("\nAll students in the system:")
        for name in self.students_list:
            age, grade = self.students_dict[name]
            print(f"Name: {name}, Age: {age}, Grade: {grade}")

# Example usage
if __name__ == "__main__":
    system = StudentManagementSystem()

    while True:
        print("\nStudent Information Management System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Remove Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            system.add_student(name, age, grade)
            print("Student added successfully!")

        elif choice == "2":
            name = input("Enter student name to search: ")
            system.search_student(name)

        elif choice == "3":
            name = input("Enter student name to remove: ")
            system.remove_student(name)

        elif choice == "4":
            system.display_all_students()

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
