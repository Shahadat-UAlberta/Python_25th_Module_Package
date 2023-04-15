from math_ops import basic_ops
from math_ops import advanced_ops

print('What operation do you want to perform?')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Exponential')
print('6. Logarithms')
print('7. Square Roots')
print('Enter operation: 1/2/3/4/5/6/7 -->')

operation = int(input())

if operation == 1:
    num1 = float(input())
    num2 = float(input())
    print(basic_ops.addition(num1, num2))

elif operation == 2:
    num1 = float(input())
    num2 = float(input())
    print(basic_ops.subtraction(num1, num2))

elif operation == 3:
    num1 = float(input())
    num2 = float(input())
    print(basic_ops.multiplication(num1, num2))

elif operation == 4:
    num1 = float(input())
    num2 = float(input())
    print(basic_ops.division(num1, num2))

elif operation == 5:
    num1 = float(input('Enter base: '))
    num2 = float(input('Enter power: '))
    print(advanced_ops.exponents(num1, num2))

elif operation == 6:
    num1 = float(input('Enter number: '))
    print(advanced_ops.logarithms(num1))

elif operation == 7:
    num1 = float(input('Enter number: '))
    print(advanced_ops.square_root(num1))

else:
    print('Inavlid operation. Please input a valid operation --. 1/2/3/4/5/6/7')
