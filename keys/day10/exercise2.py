# Exercise 2: Write a custom module with a function and import it in another program.

# Create a file named `mymodule.py` with the following content:
# def greet(name):
#     return f"Hello, {name}!"

# In this file, import and use the custom module:
import mymodule

message = mymodule.greet("Alice")
print(message)