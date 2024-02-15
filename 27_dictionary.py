'''
-dictionary is ordered collection of data type
-items are key-value pair enclosed in curly braces separated by comma
- store multiple items in single variable
-do not allow duplicate
'''

info = {'name': 'ishwari', 'age': 20, 'class': 'TYA'}
print(info)  # output:{'name': 'ishwari', 'age': 20, 'class': 'TYA'}

print(info['age'])  # output:20

# ovewrite existing value
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)  # output:{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# length of dictionary
print(len(thisdict))  # output:3

# string,int,boolean,list data type
car = {
    'brand': 'ford',
    'electric': False,
    'year': 1994,
    'colors': ['white', 'red', 'blue']
}
print(car)
print(type(car))
