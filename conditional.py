num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1>num2 and num1>num3:
    print("the number one is bigger")
elif num2>num3 and num2>num1:
    print("the second number is bigger")
elif num3>num1 and num3>num2:
    print("the third number is bigger")
else:
    print("two or three numbers are equal")
