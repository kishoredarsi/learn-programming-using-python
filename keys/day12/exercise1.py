# Exercise 2: Write a program that reads from a file.

# Read from a file named 'robots.txt' in the same directory as the program.

# Open the file in read mode
with open('robots.txt', 'r') as file:
    # Read the content of the file
    content = file.read()
    # Print the content of the file
    print(content)
    # Close the file
    file.close()

