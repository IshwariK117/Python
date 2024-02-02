# you just have to specify the index where you just have to specify index where you want to replace
names = ["harry", "sarah", "nadia", "steve"]
print(names)
names[2] = "mily"
print(names)  # output:['harry', 'sarah', 'mily', 'steve']

# we can also chnage more than single item at once
names[2:3] = ["juan", "john"]
print(names)

# what if we have more items o be replaced than the index range provided,it will
print(names)
# ['harry', 'sarah', 'juan', 'john', 'steve']
names[2:3] = ["juan", "john", "Bruno", "Merry", "Rosi"]
print(names)
# output: ['harry', 'sarah', 'juan', 'john', 'Bruno', 'Merry', 'Rosi', 'john', 'steve']
