# Exercise 2: Write a class that inherits from another class and adds a new method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

student = Student("Bob", 20, "S12345")
student.display_student()