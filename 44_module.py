'''
-it is like library ,file which contain functions,methods that we want to include in our file
'''
import math

# BUILT-IN MODULE
print("sin 0=", math.sin(0))
print("Sin 30 =", math.sin(math.pi / 6))
print("Sin 45 =", math.sin(math.pi / 4))
print("Sin 60 =", math.sin(math.pi / 3))
print("Sin 90 =", math.sin(math.pi / 2))

# USER-DEFINED MODULE
import my_module

my_module.greetings(" ishwari")

a = my_module.person1["age"]
print(a)


from my_module import add,sub,mul,div

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("Addition", add(num1, num2))
print("Subtraction", sub(num1, num2))
print("Multiplication", mul(num1, num2))
print("Division", div(num1, num2))