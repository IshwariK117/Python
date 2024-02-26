# append()-add element at end of list
list1 = [1, 2, 3, 4]
list1.append(5)
print(list1)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

# clear()-remove all the element from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

# copy()-return copy of list
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(fruits)

# count()-count number of element with specified value
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# extend()-Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# index()-Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# insert()-Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# pop()-Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# remove()-remove the first item with specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# reverse()-reverse the order of list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# sort()-Sorts the list
fruits = ['apple', 'banana', 'cherry']
fruits.sort()
print(fruits)
