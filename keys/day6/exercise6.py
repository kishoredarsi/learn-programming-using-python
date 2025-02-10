# Exercise6: Write a program to find the multiplication of first 10 integers.

# Hint: Use for loop to iterate through the range of 1 to 11 and multiply each number with the previous number.
for i in range(1, 11):
    if i == 1:
        result = i
    else:
        result *= i

# Expected Output:
# 3628800

print(f"Multiplcation of numbers from 1 to 10: {result}")
