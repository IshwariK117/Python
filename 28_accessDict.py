# ACCESS OR CHANGE ITEMS
'''
-we can access items by refering key names in dictionary inside square brackets
'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict['model'])  # output:Mustang
print(thisdict['brand'])  # output:Ford

x = thisdict.get('model')
print(x)  # output:Mustang

# key() method will return all the keys in dictionary
y = thisdict.keys()
print(y)  # output:dict_keys(['brand', 'model', 'year'])

z = thisdict.values()
print(z)  # output:dict_values(['Ford', 'Mustang', 1964])

# change in original list
thisdict['year'] = 2000
print(thisdict)
