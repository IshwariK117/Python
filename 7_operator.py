# arithmetic operator
# lambda is cstomizable variable ..we can do operation in different scenario
add = lambda a, b: a + b
result = add(2, 3)
print(result)

subtract = lambda a, b: a - b
result = subtract(3, 2)
print(result)

multiply = lambda a, b: a * b
result = multiply(2, 3)
print(result)

div = lambda a, b: a / b
result = div(10, 5)
print(result)

rem = lambda a, b: a % b
result = rem(10, 5)
print(result)

exp = lambda a, b: a ** b
result = exp(2, 5)
print(result)

flr = lambda a, b: a // b
result = flr(10, 4)
print(result)

# Assignment operator - =,+=,-=,*=,/=,%=,**=,//=
res = 30
print(res)
res += 6
print(res)
res -= 6
print(res)


# comparison operator
def compare_values(a, b):
    if a == b:
        return 'equal'
    elif a < b:
        return 'less than b'
    elif a > b:
        return 'greater than b'
    elif a <= b:
        return 'less than equal to b'
    elif a >= b:
        return 'greater than equal to'
    else:
        return 'not mathing'


res = compare_values(10, 20)
print(res)

# logical operator
a = True
b = False

result = a and b
print(result)  # Output: False
result = a or b
print(result)
result = not a
print(result)
