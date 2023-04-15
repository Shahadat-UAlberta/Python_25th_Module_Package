#Create a Python package called "math_ops". Inside the package, create a module called "basic_ops"
# that defines functions for basic arithmetic operations (addition, subtraction, multiplication,
# and division). Create another module called "advanced_ops" that defines functions for advanced
# operations (exponents, logarithms, and square roots).

# Write a program that imports the "basic_ops" module from the "math_ops" package and uses the functions
# to perform some basic arithmetic operations (e.g., add two numbers, multiply two numbers).

# Write a program that imports the "advanced_ops" module from the "math_ops" package and uses the
# functions to perform some advanced arithmetic operations (e.g., calculate the logarithm of a number).

# W4. rite a program that imports both the "basic_ops" and "advanced_ops" modules from the "math_ops"
# package and uses the functions to perform a variety of arithmetic operations.

from math_ops import sum, sub, mul, div
a= int(input("Enter an integer- "))
b= int(input("Enter 2nd integer- "))
print(sum(a,b))
print(div(a,b))
print(mul(a,b))

from math_ops import root, log, ex
num= int(input("Ente a number- "))
print(root(num))
print(log(num))