# Import the basic_ops module from the math_ops package
from math_ops import basic_ops

# Use the functions to perform some basic arithmetic operations
print(basic_ops.add(2, 3))         # Output: 5
print(basic_ops.multiply(4, 5))    # Output: 20
# Import the advanced_ops module from the math_ops package
from math_ops import advanced_ops

# Use the functions to perform some advanced arithmetic operations
print(advanced_ops.power(2, 3))             # Output: 8
print(advanced_ops.logarithm(100, 10))      # Output: 2.0
print(advanced_ops.square_root(25))         # Output: 5.0
# Import both the basic_ops and advanced_ops modules from the math_ops package
from math_ops import basic_ops, advanced_ops

# Use the functions to perform a variety of arithmetic operations
print(basic_ops.add(2, 3))                        # Output: 5
print(basic_ops.multiply(4, 5))                   # Output: 20
print(advanced_ops.power(2, 3))                    # Output: 8
print(advanced_ops.logarithm(100, 10))             # Output: 2.0
print(advanced_ops.square_root(25))                # Output: 5.0
print(basic_ops.divide(10, 2))                     # Output: ValueError: Cannot divide by zero
