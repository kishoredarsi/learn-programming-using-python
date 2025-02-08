# Exercise 5: Write a program to count list of odd and even numbers in a given list of numbers.

# Initialize a list of numbers
# Initialize counters for odd and even numbers
# Loop through each number in the list
# If the number is even, increment the even counter
# If the number is odd, increment the odd counter
# Print the counts of odd and even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_count = 0
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Odd numbers count:", odd_count)
print("Even numbers count:", even_count)