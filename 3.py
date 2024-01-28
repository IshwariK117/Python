# Define the basic operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


# Define a function to perform operations
def perform_operation(operation, x, y):
    return operation(x, y)


# Define a function to compose two functions
def compose(f, g):
    return lambda x, y: f(g(x, y))


# Create a dictionary of operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Get user input for operation
operator = input("Enter which operation do you want to perform (+, -, *, /): ")

# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the selected operation if it exists
if operator in operations:
    result = perform_operation(operations[operator], num1, num2)
    print("Result:", result)
else:
    print("Invalid operation")
