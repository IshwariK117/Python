# sort():sort the list in ascending order
colors = ["violet", "indigo", "blue", "green"]
colors.sort()
print(colors)  # output:['blue', 'green', 'indigo', 'violet']

num = [73, 44, 23, 84, 55, 15, 64, 63, 77, 15, 34, 55]
num.sort()
print(num)  # output:[15, 23, 34, 44, 55, 63, 64, 73, 77, 84]

# print the list in descending order
num.sort(reverse=True)
print(num)  # output:[84, 77, 73, 64, 63, 55, 44, 34, 23, 15]

# index():this method return the index of the first occurence of list
print(colors.index("green"))  # output:1

# count():returns the count of number of items with given value
print(num.count(55))  # output:2

# copy():return the copy of the list ,perform operation on list without modifying original list
newlist = colors.copy()
print(newlist)       #output:['blue', 'green', 'indigo', 'violet']

