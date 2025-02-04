# Exercise 3: Perform various string operations on an English sentence.

sentence = "The quick brown fox jumps over the lazy dog"

# Find the length of the sentence
length = len(sentence)
print("Length of the sentence:", length)

# Convert the sentence to lower case
lower_case = sentence.lower()
print("Lower case:", lower_case)

# Convert the sentence to upper case
upper_case = sentence.upper()
print("Upper case:", upper_case)

# Split the sentence by space
words = sentence.split(" ")
print("Words:", words)

# Replace a substring in the sentence
replaced_sentence = sentence.replace("fox", "cat")
print("Replaced sentence:", replaced_sentence)