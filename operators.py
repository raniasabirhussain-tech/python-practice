# BODMAS Demonstration in Python
# This program demonstrates how Python calculates arithmetic expressions
# following BODMAS rules (Brackets, Orders, Division, Multiplication, Addition, Subtraction)

# Take three numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Expression without brackets (BODMAS applies automatically)
result_without_brackets = num1 + num2 - num3 / num1

# Expression with a different combination (division first, then subtraction and addition)
result_with_brackets = num1 - num2 + num3 / num2

# Print the results clearly
print(f"Result without brackets: {result_without_brackets}")
print(f"Result with brackets: {result_with_brackets}")
