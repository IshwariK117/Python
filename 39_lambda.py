'''
-small anonymous function
-can take any no.of arguments but have only one expression
lambda arguments:expression
'''

x=lambda a:a+10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def my_func(n):
    return lambda a:a*n

func=my_func(5)
print(func(3))