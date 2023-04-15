def divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 'Cannot divide by zero'


