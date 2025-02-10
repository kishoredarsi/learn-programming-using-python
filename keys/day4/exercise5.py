# Exercise5: Write a program to print the food category using match case.

# Assign a food to a variable
food = "Pizza"

# Use match case to print the food category
# Use the following categories:
# - Italian
# - Japanese
# - Mexican
# - Indian
# - Chinese
# - American
# - Other
# Print the category of the food

match food:
    case "Pizza":
        print("Italian")
    case "Sushi":
        print("Japanese")
    case "Taco":
        print("Mexican")
    case "Curry":
        print("Indian")
    case "Dim Sum":
        print("Chinese")
    case "Hamburger":
        print("American")
    case _:
        print("Other")

# Output: Italian
# The output is Italian because the food is Pizza and the category is Italian.