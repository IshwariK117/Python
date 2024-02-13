# copy():we can use copy method to copy the content from one to another dictionary
info = {'name': 'Anupam', 'age': 44, 'eligible': True, 'DOB': 1980}
newDict = info.copy()
print(newDict)  # output:{'name': 'Anupam', 'age': 44, 'eligible': True, 'DOB': 1980}

# or we can use dict to create/copy dictionary
newDictionary = dict(info)
print(newDictionary)  # output:{'name': 'Anupam', 'age': 44, 'eligible': True, 'DOB': 1980}

for dict in newDict:
    print(newDict[dict])
'''
Anupam
44
True
1980
'''

for x in newDict.keys():
  print(x)

for x, y in newDict.items():
  print(x, y)
'''
name Anupam
age 44
eligible True
DOB 1980
'''
