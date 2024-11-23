def max(value):
    if not value:
        return None
    max_value = value[0]
    for item in value[1:]:
        if max_value < item:
            max_value = item
    return max_value


def average(value):
    if not value:
        return None
    result = 0
    for item in value:
        result += item
    return round(result / len(value), 2)


def min(value):
    if not value:
        return None
    min_value = value[0]
    for item in value[1:]:
        if min_value > item:
            min_value = item
    return min_value


def sort(value):
    if not value:
        return None
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
