def divide(numerator, denominator):
    try:
        result = ( numerator / denominator )
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

result = divide(numerator, denominator)
print(str(result))
