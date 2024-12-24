import math


def sum(*args):
    result = 0
    for item in args:
        result += item
    return result


def subtraction(number=0, *args):
    result = number
    for item in args:
        result -= item
    return result


def multiply(*args):
    result = 1
    for item in args:
        result *= item
    return result


def divide(number=0, *args):
    if 0 in args:
        return None
    result = number
    for item in args:
        result /= item
    return result


def factorial(value):
    if value <= 1:
        return 1
    else:
        return (value * factorial(value - 1))


def pow(number=0, *args):
    result = number
    for item in args:
        result **= item
    return result


def degrees_to_radians(value):
    return round(value * math.pi / 180, 2)


def radians_to_degrees(value):
    return round(value * 180 / math.pi, 2)


def log(value, base=2):
    if base < 2 or value < 1:
        return None
    result = 0
    while base**result <= value:
        result += 1
    return result - 1
