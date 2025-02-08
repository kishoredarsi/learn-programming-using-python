# Exercise 4: Write a program to print GCD (greatest common divisor) of given two numbers.

# Get two numbers from the user
# Define a function to calculate the GCD (greatest common divisor) of two numbers
# Print the GCD

# Exercise 4: Write a program to print GCD (greatest common divisor) of given two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))