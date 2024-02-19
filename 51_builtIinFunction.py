# abs()-return absolute value of number
x = abs(-5.43)
print(x)

y = abs(3 + 5j)
print(y)

# all()-check all the items in list are true , if yes return true otherwise if empty return false
mylist = ["hello", "namaskar", "bonjur"]
print(all(mylist))

mytuple = (0, True, False)
x = all(mytuple)
print(x)  # Returns False because both the first and the third items are False

# any()-check if one of the item in list are true
mytuple = (1, 0, True)
print(any(mytuple))

# bool()-return boolean value of specified object
x = bool(0)
print(x)  # output:False

# chr()-Get the character that represents the unicode :

x = chr(97)
print(x)


# dir()-return all specified properties and objects
class person:
    name = "john"
    age: 34


print(
    dir(person))  # output: ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']

# filter()- items are filtered throgh iterable object
ages = [12, 34, 54, 13, 53]


def func(x):
    if x < 18:
        return True
    else:
        return False


adults = filter(func, ages)

for x in adults:
    print(x)

# format()-format the specified value
x = format(0.5, '%')
print(x)

# hex()-convert number into hexadecimal value
x = hex(116)
print(x)

# id()-return unique id of object
mytuple = (1, 3, 4)
print(id(mytuple))

# input()-allwing the user input
#x=input("Enter your name")
print("hello ",x)

#iter()-return an iterator object
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

#len()-return length of an object
print(len(mytuple))

#max()-return item which has highest value
x=max(3,5)
print(x)
x = max("Mike", "John", "Vicky")
print(x)

#min()-return item which has lowest value
x=min(3,5)
print(x)
x =min("Mike", "John", "Vicky")
print(x)

#pow()-return the value of x to the power y
x = pow(4, 3)
print(x)

#return slice object
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

#sorted()-return a sorted list
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

#str()-convert specified value to string
x = str(3.5)
print(x)



