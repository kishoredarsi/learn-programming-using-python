# Exercise 2: Write a program to print whether the number is even or odd number.

# Get the number from the user
# Convert the input to a float
# Store the number in a variable
number = float(input("Enter a number: "))

# Check if the number is even or odd
# If the number is divisible by 2, it is an even number
# If the number is not divisible by 2, it is an odd number
# Print the result
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

