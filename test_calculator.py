
from Calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulus,
    maximum,
    minimum,
    average,
    is_even
)

# Addition tests
assert add(2, 3) == 5
assert add(-2, -3) == -5
assert add(10, 0) == 10

# Subtraction tests
assert subtract(10, 5) == 5
assert subtract(5, 10) == -5

# Multiplication tests
assert multiply(4, 3) == 12
assert multiply(10, 0) == 0

# Division tests
assert divide(10, 2) == 5
assert divide(7, 2) == 3.5

# Power tests
assert power(2, 3) == 8
assert power(5, 2) == 25

# Modulus tests
assert modulus(10, 3) == 1
assert modulus(8, 4) == 0

# Maximum and minimum tests
assert maximum(10, 20) == 20
assert minimum(10, 20) == 10

# Average tests
assert average(10, 20) == 15

# Even number tests
assert is_even(4) == True
assert is_even(7) == False
assert is_even(0) == True

# Error handling tests
try:
    divide(10, 0)
    assert False, "Expected ValueError for division by zero"
except ValueError:
    pass

try:
    modulus(10, 0)
    assert False, "Expected ValueError for modulus by zero"
except ValueError:
    pass

print("All 20+ tests passed!")
