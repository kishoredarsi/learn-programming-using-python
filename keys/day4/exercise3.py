# Exercise 3: Write a program to print whether the student received A or A+ grade.

# Get the marks from the user
# Convert the input to a float
# Store the marks in a variable
marks = float(input("Enter the marks: "))

# Check if the marks are greater than or equal to 90
# If the marks are greater than or equal to 90, the student received A+ grade
# If the marks are less than 90 and greater than or equal to 80, the student received A grade
# Print the result

if marks >= 90:
    print("The student received A+ grade")
elif marks >= 80:
    print("The student received A grade")
else:
    print("The student did not receive an A or A+ grade")