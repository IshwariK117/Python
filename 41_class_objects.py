# class is like bluprint or template for creating object
class my_class:
    print("hi")


print(my_class)


class main:
    x = 5


p1 = main()
print(p1.x)


# __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = person("ishwari", 20)
print(p1.name)


# The __str__() function controls what should be returned when the class object is represented as a string.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)


# Use the words mysillyobject and abc instead of self:

class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()
