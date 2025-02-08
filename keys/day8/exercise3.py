# Exercise 3: Write a program to print LCM (least common multiple) of given two numbers.

# Get two numbers from the user
# Define a function to calculate the GCD (greatest common divisor) of two numbers
# Use the GCD to calculate the LCM
# Print the LCM

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))