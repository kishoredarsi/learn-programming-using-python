# Exercise 2: Write a program to write to a file.

# A paragraph is given below. Write a program to write the paragraph to a file named 'paragraph.txt' in the same directory as the program.

# Paragraph:
paragraph = """Python is an interpreted, high-level, general-purpose programming language. 
Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes 
code readability with its notable use of significant whitespace. Its language constructs and 
object-oriented approach aim to help programmers write clear, logical code for small and 
large-scale projects."""

# Open the file in write mode
with open('paragraph.txt', 'w') as file:
    # Write the paragraph to the file
    file.write(paragraph)
    # Close the file
    file.close()
