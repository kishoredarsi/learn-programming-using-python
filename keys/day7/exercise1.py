# Exercise 1: Write a program to print increasing sequence of character in each line.

# Get the character from the user
# Use nested loops to print the increasing sequence of the character
# Hint: Use the ord() and chr() functions to convert between characters and their ASCII values

# Exercise 1: Write a program to print increasing sequence of character in each line.

char = input("Enter a character: ").upper()
for i in range(1, ord(char) - ord('A') + 2):
    print("".join(chr(ord('A') + j) for j in range(i)))