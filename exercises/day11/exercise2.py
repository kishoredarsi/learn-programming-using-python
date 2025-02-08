# Exercise 2: Write a program that reads from a file and writes to a file.

# Write to a file
with open("output.txt", "w") as file:
    file.write("Hello, file!")

# Read from a file
with open("output.txt", "r") as file:
    content = file.read()
    print("File content:", content)