# since tuple is immutable we cant directly add,rove or update...first we convert to list and after agai convertto tuple
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")  # add item
temp.pop(3)  # remove item
temp[2] = "Finland"  # change item
countries = tuple(temp)
print(countries)

'''
Unpack Tuples
he process of assigning the tuple items as values to variables.
'''
info = ("Marcus", 20, "MIT")
(name, age, university) = info
print("Name:", name)
print("Age:", age)
print("Studies at:", university)


#But what if we have more number of items then the variables?
fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, bird, fish) = fauna
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)
