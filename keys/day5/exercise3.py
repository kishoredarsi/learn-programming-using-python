# Exercise 4: Split a sentence, remove spaces from each word, capitalize each word, and join the words back into a string.

sentence = "The quick brown fox jumps over the lazy dog"

# Split the sentence by space
words = sentence.split(" ")

# Remove spaces from each word and capitalize each word
processed_words = [word.strip().capitalize() for word in words]

# Join the words back into a string
result_sentence = "".join(processed_words)

print("Processed sentence:", result_sentence)