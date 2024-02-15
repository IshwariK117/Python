#return back to the main functiom
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))

#recursion:function call itsef
def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

print("factorial is",factorial(7))


