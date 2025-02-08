# Exercise 2: Write a program to convert given character into a position number in the alphabets.

# Get the character from the user
# Convert the character to its position number in the alphabet
# Hint: Use the ord() function and subtract ord('a') or ord('A') accordingly
# Print the position number

char = input("Enter a character: ").lower()
position = ord(char) - ord('a') + 1

print(f"The position of '{char}' in the alphabet is {position}.")