# Exercise 3: Write a program to swap two numbers.

# Get two numbers from the user
# Swap the numbers using a temporary variable
# Print the swapped numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swapping using a temporary variable
temp = num1
num1 = num2
num2 = temp

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)