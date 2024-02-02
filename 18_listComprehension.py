# List comprehension: used for creating new list from otheriterables like lists ,tuple,dictionaries,sets and even in arrays and strings
'''
syntax:
list:[expression(item) for item in iterable if condition]
expressiom:it is the item which is being iterated
iterable:it can be tuple,list,dictionary and set
condition:condition check if the item should be added to new list or not
'''

# accepts the item with the the small letter "o" in the new list
colors = ["red", "green", "yellow", "pink", "orange"]
colorswith_o = [item for item in colors if "o" in item]
print(colorswith_o)  # output: ['yellow', 'orange']

# accept items which have more than 4 letters
moreThan_4 = [item for item in colors if (len(item) > 4)]
print("more than 4 items are:", moreThan_4)  # output: more than 4 items are: ['green', 'yellow', 'orange']

