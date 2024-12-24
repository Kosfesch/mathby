# Mathby

[![Python CI](https://github.com/Kosfesch/mathby/actions/workflows/check.yaml/badge.svg)](https://github.com/Kosfesch/mathby/actions/workflows/check.yaml)

[![Maintainability](https://api.codeclimate.com/v1/badges/0a593dd074a40acd0386/maintainability)](https://codeclimate.com/github/Kosfesch/mathby/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/0a593dd074a40acd0386/test_coverage)](https://codeclimate.com/github/Kosfesch/mathby/test_coverage)

## Description

Library with simple mathematical functions.

## Setup
```bash
git clone git@github.com:Kosfesch/mathby.git
cd mathby
make install
```

## Using

```python
from math_lib import arithmetics, collection, figures

arithmetics.sum(3, 4) # 7
collection.max([24, 10, 7, 6, 0]) # 24
figures.square_perimeter(3) # 12
```

## Modules and functions

Functions list:

- [arithmetics.sum()](#sum)
- [arithmetics.subtraction()](#subtraction)
- [arithmetics.multiply()](#multiply)
- [arithmetics.divide()](#divide)
- [arithmetics.factorial()](#factorial)
- [arithmetics.pow()](#pow)
- [arithmetics.degrees_to_radians()](#degrees_to_radians)
- [arithmetics.log()](#log)
- [collection.min](#min)
- [collection.max](#max)
- [collection.average](#average)
- [collection.sort](#sort)
- [figures.circle_area](#circle_area)
- [figures.circle_perimeter](#circle_perimeter)
- [figures.square_perimeter](#square_perimeter)
- [figures.square_area](#square_area)
- [figures.triangle_perimeter](#triangle_perimeter)
- [figures.rectangle_perimeter](#rectangle_perimeter)
- [figures.rectangle_perimeter](#rectangle_perimeter)
- [figures.rectangle_area](#rectangle_area)



### arithmetics

#### sum()

*Description:* sum all the arguments.

*Arguments:* *args

*Example:*

```python
sum(3, 4) #7
sum(18, 41, 16, 8) # 83
```

#### subtraction()

*Description:* subtraction all the arguments.

*Arguments:* *args

*Example:*

```python
subtraction(18, 41, 16, 8) # -47
subtraction(-1, -6, -50) # 55
```

#### multiply()

*Description:* multiply all the arguments.

*Arguments:* *args

*Example:*

```python
multiply(10, 5) # 50
multiply(1) # 1
```

#### divide()

*Description:* divide all the arguments.

*Arguments:* *args

*Example:*

```python
divide(4, 2) # 2
divide(12, 3, 2) # 2
```

#### factorial()

*Description:* find factorial of number.

*Arguments:* value

*Example:*

```python
factorial(5) # 120
factorial(6) # 720
```

#### pow()

*Description:* pow of number.

*Arguments:* value, pow

*Example:*

```python
pow(15, 2) # 225
pow(1, 3) # 1
```

#### degrees_to_radians()

*Description:* converts from degrees to radians.

*Arguments:* value

*Example:*

```python
degrees_to_radians(1) # 0.02
degrees_to_radians(10) # 0.17
```

#### radians_to_degrees()

*Description:* converts from radians to degrees.

*Arguments:* value

*Example:*

```python
radians_to_degrees(1) # 57.30
radians_to_degrees(10) # 572.96
```

#### log()

*Description:* log of number.

*Arguments:* value1, value2

*Example:*

```python
log(16, 4) # 2
log(60, 2) # 5
```

### Collection

#### min()

*Description:* find minimal number.

*Arguments:* *args

*Example:*

```python
min([52, 23, 15, 20, 40]) # 15
min([92, -1, 73, -20, 0]) # -20
```


#### max()

*Description:* find maximal number.

*Arguments:* *args

*Example:*

```python
max([24, 10, 7, 6, 0]) # 24
max([13, 0, 1, 1, 6]) # 13
```


#### average()

*Description:* count average of numbers.

*Arguments:* *args

*Example:*

```python
average([24, 10, 7, 6, 0]) # 9.4
average([13, 0, 1, 1, 6]) # 4.2
```

#### sort()

*Description:* sort lists.

*Arguments:* *args

*Example:*

```python
sort([24, 10, 7, 6, 0]) # [0, 6, 7, 10, 24]
sort([13, 0, 1, 1, 6]) # [0, 1, 1, 6, 13]
```


### Figures


#### circle_area()

*Description:* finds circle area.

*Arguments:* number

*Example:*

```python
circle_area(3) # 28.27
circle_area(10) # 314.16
```


#### circle_perimeter()

*Description:* finds circle perimeter.

*Arguments:* number

*Example:*

```python
circle_perimeter(3) # 18.85
circle_perimeter(10) # 62.83
```


#### square_perimeter()

*Description:* finds square perimeter.

*Arguments:* number

*Example:*

```python
square_perimeter(3) # 12
square_perimeter(10) # 40
```


#### square_area()

*Description:* finds square area.

*Arguments:* number

*Example:*

```python
square_area(3) # 9
square_area(10) # 100
```


#### triangle_perimeter()

*Description:* finds triangle perimeter.

*Arguments:* number1, number2, number3

*Example:*

```python
triangle_perimeter(3, 3, 3) # 9
triangle_perimeter(10, 7, 8) # 25
```


#### rectangle_perimeter()

*Description:* finds rectangle perimeter.

*Arguments:* number1, number2

*Example:*

```python
rectangle_perimeter(3, 3) # 12
rectangle_perimeter(10, 7) # 34
```


#### rectangle_area()

*Description:* finds rectangle area.

*Arguments:* number1, number2

*Example:*

```python
rectangle_area(3, 3) # 9
rectangle_area(10, 7) # 70
```