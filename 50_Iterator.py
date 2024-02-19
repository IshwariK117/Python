#Iterators in python are used to iterate over iterable objects or container datatypes like lists, tuples, dictionaries, sets, etc.
'''

It consists of __iter__() and __next__() methods.
__iter__() : to initialize an iterator, use the __iter__() method.
__next__() : This method returns the next item of the sequence.
'''

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print("-----------------------------")
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print("---------------------------")




#Using inbuilt iterators:
string = 'Hello World'
iterObj = iter(string)

while True:
    try:
        char1 = next(iterObj)
        print(char1)
    except StopIteration:
        break