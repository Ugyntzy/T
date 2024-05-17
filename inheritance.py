class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students' work.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")


class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying for {self.course}.")

    def attend_class(self):
        print(f"{self.name} is attending {self.course} class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam for {self.course}.")


# Example usage:
teacher1 = Teacher("Dr. Smith", 40, "12345", "Math", 60000, "Math Department", "Professor")
student1 = Student("Alice", 20, "67890", "S123", "Computer Science", 2, 3.8)

teacher1.walk()
teacher1.teach()
student1.talk()
student1.study()
