# Take numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Arithmetic calculations demonstrating BODMAS
result_without_brackets = num1 + num2 - num3 / num1
result_with_brackets = num1 - num2 + num3 / num2

# Print results clearly
print(f"Result without brackets: {result_without_brackets}")
print(f"Result with brackets: {result_with_brackets}")
print(f"Multiplication of first two numbers: {num1 * num2}")
print(f"Addition of all three numbers: {num1 + num2 + num3}")
print(f"Combined multiplication of all three numbers: {num1 * num2 * num3}")
