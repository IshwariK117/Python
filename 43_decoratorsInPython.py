'''
-decorator is a function that takes another function as an argument
and returns new function that modifies the behaviout of original function
-used to modify a function
-they are way to extend the functionality of function without modifying its source code
'''


def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")

    return mfx


@greet
def hello():
    print('hello')


def add(a, b):
    print(a + b)


hello()



print("---------------------------")
def my_decorator(func):
    def wrapper():
        print("someting happen before function")
        func()
        print("something happen after function")
    return wrapper


@my_decorator
def say_hello():           #this function to be decorated
    print("hello")

#call the decorated function
say_hello()






