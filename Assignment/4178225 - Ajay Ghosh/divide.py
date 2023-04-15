def divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 'Cannot divide by zero'

num1 = int(input())
num2 = int(input())
print(divide(num1, num2))
