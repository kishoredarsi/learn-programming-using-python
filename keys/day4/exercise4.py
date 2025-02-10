# Exercise4: Write a program to print the grade for a student score.

# Assign a score to a variable
score = 85

# Hint: Use if-elif-else statement to check the score and print the grade
# Hint: Use the following grading system:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F

# Write your code here

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score <= 89:
    print("Grade: B")
elif score >= 70 and score <= 79:
    print("Grade: C")
elif score >= 60 and score <= 69:
    print("Grade: D")
else:
    print("Grade: F")
    
# Expected output:
# Grade: B