# constructor are used to instantiating the object
# the task is to assign values to data members
# Python the __init__() method is called the constructor and is always called when an object is created.
'''
syntax:
def __init__(self):
    # body of the constructor
'''

'''
-two types of constructor
1.default
2.parameterized
'''


# DEFAULT CONSTRUCTOR
class my_class:
    def __init__(self):
        print("Default constructor called")


obj = my_class()


class MyOtherClass:
    pass


obj = MyOtherClass()

# PARAMETERIZED CONSTRUCTOR

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_info(self):
        print(f"{self.name},{self.age}")

obj1=person("ishwari",20)
obj1.print_info()

