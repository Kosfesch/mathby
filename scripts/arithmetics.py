def sum(*args):
    result = 0
    for item in args:
        result += item
    return result


def substraction(number=0, *args):
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
