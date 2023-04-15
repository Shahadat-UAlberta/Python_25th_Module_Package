from math_ops import basic_ops

print('What operation do you want to perform?')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('Enter operation: 1/2/3/4 -->')

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

else:
    print('Inavlid operation. Please input a valid operation --. 1/2/3/4')
