# Exercise5: Write a program to find a standard deviation of list of integers.


# Hint: The standard deviation of a list of numbers is calculated as:
# 1. Calculate the mean of the list.
# 2. Calculate the squared differences between each number and the mean.
# 3. Sum the squared differences.
# 4. Divide the sum by the number of elements in the list.
# 5. Take the square root of the result.

xx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean = sum(xx) / len(xx)
squared_diff = [(x - mean) ** 2 for x in xx]
sum_squared_diff = sum(squared_diff)
variance = sum_squared_diff / len(xx)
std_dev = variance ** 0.5
print(f"Standard deviation of list is: {std_dev}")

