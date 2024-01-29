# Scope of variable: it is the area where the variable is declared, so it can be local or global.

shape = 'circle'  # Global variable


def shape_of_object():
    shape1 = 'square'  # Local variable
    color = 'red'  # Local variable
    print(shape + ' is a global variable')
    print(shape1 + ' is a local variable')
    print(color + " is a local variable")


# Call the function
shape_of_object()
print(shape + ' is global variable') #shape is global varible so it will be displayed
print(shape1 + 'is local variable')   #shape1 is local variable so it will not displayed

