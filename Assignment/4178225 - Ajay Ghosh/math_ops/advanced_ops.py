import math

def exponents(base, power):
    return base ** power

def logarithms(num):
    try:
        return math.log(num)

    except Exception as e:
        print('Please enter a valid number greater than 0')

def square_root(num):
    try:
        return math.sqrt(num)

    except Exception as e:
        print("Please enter a valid number greater than or equal 0")