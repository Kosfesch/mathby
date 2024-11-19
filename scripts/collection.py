def max(value):
    max_value = 0
    for item in value:
        if max_value < item:
            max_value = item
    return max_value


def average(value):
    result = 0
    for item in value:
        result += item
    return round(result / len(value), 2)


def min(value):
    min_value = 0
    for item in value:
        if min_value > item:
            min_value = item
    return min_value


def sort(value):
    step = len(value) - 1
    swaped = True
    while swaped:
        swaped = False
        for i in range(step):
            if value[i] > value[i + 1]:
                value[i], value[i + 1] = value[i + 1], value[i]
                swaped = True
        step -= 1
    return value
