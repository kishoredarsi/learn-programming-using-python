# Exercise 4: Write a program to find biggest number among given numbers.

# Get a list of numbers from the user
# Initialize a variable to store the biggest number
# Loop through each number in the list
# If the current number is greater than the biggest number, update the biggest number
# Print the biggest number


numbers = list(map(float, input("Enter numbers separated by space: ").split()))
biggest_number = max(numbers)

print("The biggest number is:", biggest_number)