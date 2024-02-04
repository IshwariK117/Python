'''
# set():sets are unordered collection of data items
- they store multiple items in single variable
- enclosed in square brackets {}  separetd by comma ,
- unique items are there
- immutable
'''

myset = {"apple", "banana", "cherry"}
print(type(myset))

info = {"cars", 54, 9.0, True}
print(info)

# accesing set items -using for loops
for i in info:
    print(i)

boolean = {1, True}
print(boolean)  # 1 and True are same in sets and treated as duplicate

thisset = {"apple", "banana", "cherry"}
print(len(thisset))
