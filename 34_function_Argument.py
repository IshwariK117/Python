'''
1.default argument-We can provide a default value while creating a function. This way the function assumes
a default value even if a value is not provided in the function call for that argument.

2.keyword argument-can provide arguments with key = value,
this way the interpreter recognizes the arguments by the parameter name.

3.required argument-
In case we don’t pass the arguments with a key = value syntax,
then it is necessary to pass the arguments in the correct positional order

4.variable-length argument-
'''


# Default arguments:
def my_func(fname, lname="doe"):
    print("hello", fname, lname)


my_func("john")


# keyword argument
def name(fname, lname):
    print("Hello,", fname, lname)


name(lname="Wesker", fname="Jade")


# required argument
def name(fname, lname):
    print("hey", fname, lname)


name("peter", "quill")


# variable length argument
# 1.arbitrary argument

def my_func(*name):
    print("arbitrary argument:", name[0], name[1], name[2])


my_func("peter", "john", "wesker")


# keyword argument

def my_func(**name):
    print("keyword argument:", name["fname"], name["mname"], name["lname"])


my_func(fname='peter', mname='wesker', lname='doe')
