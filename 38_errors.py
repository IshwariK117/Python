'''
#syntax error
eval===5
print(eval)
'''

try:
    eval('x === 5')
except SyntaxError:
    print("SyntaxError: Invalid syntax")

'''
indentation error
if True:
print("hello")
'''

try:
    if True:
        print("Indentation error")
except IndentationError:
    print("IndentationError: Incorrect indentation")

'''
nameError
print(my_var)
'''
try:
    print(my_var)
except:
    print("nameerror:variable is not defined")

'''
typeerror
print(5+"5")
'''

try:
    print(5 + "5")
except TypeError:
    print("TypeError: unsupported operand type(s) for +: 'str' and 'int'")

'''
valueError
print(int("hi"))
'''
try:
    print(int("hi"))
except:
    print("valueError")

'''
keyError
my_dict={'a':3,'b':4}
print(my_dict['c'])
'''
try:
    my_dict = {'a': 3, 'b': 4}
    print(my_dict['c'])
except:
    print("keyerror occured")

'''
indexError
list=[1,2,3,4]
print(list[5])
'''
try:
    list = [1, 2, 3, 4]
    print(list[5])
except:
    print("index out of range")

'''
zerodivisionError
a=10
b=0
print(a/b)
'''

try:
    a = 10
    b = 0
    print(a / b)
except:
    print("divide by zero")
