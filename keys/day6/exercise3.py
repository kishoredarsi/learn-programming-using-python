# Exercise 3: Write a program to count number of occurrences of letter a in a given sentence.

# Get the sentence from the user
# Initialize a counter variable
# Loop through each character in the sentence
# If the character is 'a' or 'A', increment the counter
# Print the count

sentence = input("Enter a sentence: ")
count = sentence.lower().count('a')

print(f"The number of occurrences of 'a' in the sentence is {count}.")