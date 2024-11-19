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
        raise ValueError('Can\'t divide by zero')
    result = number
    for item in args:
        result /= item
    return result
