# add key in dictionary done by creating new key and assigning new value
info = {'name': 'sakshi', 'age': 19, 'eligible': True}
print(info)

info['class'] = 'TYA'
print(info)  # output:{'name': 'sakshi', 'age': 19, 'eligible': True, 'class': 'TYA'}

# by using update() method also we can add items
info.update({'dob': '11 July'})
print(info)  # output: {'name': 'sakshi', 'age': 19, 'eligible': True, 'class': 'TYA', 'dob': '11 July'}

# remove item in dictionary
# pop():removes given key-value pair from dictionary
info.pop('dob')
print(info)  # output:{'name': 'sakshi', 'age': 19, 'eligible': True, 'class': 'TYA'}

# popitem():remove last key-value pair from dictionary
info.popitem()
print(info)  # output:{'name': 'sakshi', 'age': 19, 'eligible': True}

# clear():remove all item from dictionary
info.clear()
print(info)  # output:{}
