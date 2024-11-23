from scripts.simple import sum, divide, substraction, multiply


def test_sum():
    assert sum(1, 2, 3, 5) == 11
    assert sum(1) == 1
    assert sum(18, 41, 16, 8) == 83
    assert sum(-1, -6, -50, -32) == -89


def test_divide():
    assert divide(4, 2) == 2
    assert divide(12, 3, 2) == 2
    assert divide(100, 10, 10) == 1
    assert divide(500, 10, 5, 2) == 5
    assert divide(0, 2) == 0
    assert divide(5, 0) is None


def test_substraction():
    assert substraction(10, 5) == 5
    assert substraction(1) == 1
    assert substraction(18, 41, 16, 8) == -47
    assert substraction(-1, -6, -50) == 55


def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(1) == 1
    assert multiply(18, 41, 16, 8) == 94464
    assert multiply(-1, -6, -50) == -300
    assert multiply(16, 0) == 0
    assert multiply(28, 1) == 28