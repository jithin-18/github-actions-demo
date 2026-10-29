
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot calculate modulus with zero")
    return a % b


def maximum(a, b):
    return max(a, b)


def minimum(a, b):
    return min(a, b)


def average(a, b):
    return (a + b) / 2


def is_even(n):
    return n % 2 == 0
