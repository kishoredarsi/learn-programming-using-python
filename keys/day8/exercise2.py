# Exercise 2: Write a program to print average of given list of numbers.

# Get a list of numbers from the user
# Calculate the sum of the numbers
# Calculate the average by dividing the sum by the number of elements in the list
# Print the average

numbers = list(map(float, input("Enter numbers separated by space: ").split()))
average = sum(numbers) / len(numbers)

print("The average is:", average)