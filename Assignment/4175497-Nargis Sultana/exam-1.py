# Write a function called "divide" that takes two parameters, "numerator" and "denominator",
# and returns the result of the division. In the function, use a try-except block to handle
# the possibility of a division by zero. If a division by zero occurs, return a string that says
# "Cannot divide by zero".

# Write a program that prompts the user to enter two numbers, and then uses the "divide" function
# from Task 1 to divide the first number by the second number. If the division is successful,
# print the result. If a division by zero occurs, catch the exception and print the error message.

numerator = int(input("Enter an integer- "))
denominator = int(input("Enter the 2nd integer- "))
try:
    divide = numerator/denominator
    print("%.3f"%divide)
except ZeroDivisionError as z:
    print("Can not divide by zero.")
