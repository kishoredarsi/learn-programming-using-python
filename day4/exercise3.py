# Exercise 3: Split a sentence, print parts using list index, loop through words and capitalize each word.

sentence = "The quick brown fox jumps over the lazy dog"

# Split the sentence by space
words = sentence.split(" ")
print("Words:", words)

# Print parts of the sentence using list index
print("First word:", words[0])
print("Second word:", words[1])
print("Last word:", words[-1])

# Loop through the words and capitalize each word
capitalized_words = [word.capitalize() for word in words]
capitalized_sentence = " ".join(capitalized_words)
print("Capitalized sentence:", capitalized_sentence)