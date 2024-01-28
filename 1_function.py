# Function with a nested function
def Greet():
    def say_Hello():
        print("Hello")
    return say_Hello  

# Call the outer function to get the inner function
my_function = Greet()

# Call the inner function
my_function()  # Output: Hello
