#Write a program to check if a number entered by the user is greater than 100.

num1 = float(input("Enter the first number:"))
"""if num1>100:
    print("number is greater than 100")
else:
    print("number is less than 100")"""

print("number is greater than 100" if num1>100 else"number is less than 100")