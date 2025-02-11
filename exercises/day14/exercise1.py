# Exercise 1: Write a class representing a person with attributes for name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("Alice", 30)
person.display()