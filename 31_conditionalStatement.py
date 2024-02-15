'''
-if :execute block of code inside if statement if the expressin evealuates to true
-if-else:execute block of code inside if statement if the epression is true ,otherwise execute statement in else block
-elif:works on condition that is previous condition is not true then try this one
-nested if:if statement inside if statement
'''
# IF
applePrice = 180
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1kg Apples to the cart.")

# IF-ELSE
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

a = 330
b = 200
if b > a:
    print("b is greater than a")
else:
    print("b is smaller than a")

# ELIF
x = 50
if x < 0:
    print("x is negative number")
elif x == 0:
    print("x is 0")
elif x > 0:
    print("x is positive number")
    if x > 10:
        print("x is greater than 10")

# NESTED IF
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
