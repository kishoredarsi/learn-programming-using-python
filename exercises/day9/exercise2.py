# Exercise 1: Create a dictionary of favorite fruits with their colors and print each fruit with its color.

fruits = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Cherry": "Red",
    "Date": "Brown",
    "Elderberry": "Purple"
}

for fruit, color in fruits.items():
    print(f"The color of {fruit} is {color}.")