from math_ops import advanced_ops

print('What operation do you want to perform?')
print('1. Exponential')
print('2. Logarithms')
print('3. Square Roots')
print('Enter operation: 1/2/3 -->')

operation = int(input())

if operation == 1:
    num1 = float(input('Enter base: '))
    num2 = float(input('Enter power: '))
    print(advanced_ops.exponents(num1, num2))

elif operation == 2:
    num1 = float(input('Enter number: '))
    print(advanced_ops.logarithms(num1))

elif operation == 3:
    num1 = float(input('Enter number: '))
    print(advanced_ops.square_root(num1))

else:
    print('Inavlid operation. Please input a valid operation --. 1/2/3/4')
