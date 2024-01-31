# positive index
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])

# negative index
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]      [-4]     [-3]      [-2]      [-1]
print(colors[-2])
print(colors[-4])
print(colors[-1])

# We can check if a given item is present in the list. This is done using the in keyword.
colors = ['red', 'green', 'yellow', 'pink']
if 'yellow' in colors:
    print("yellow is present")
else:
    print("not present")

# range of index: we can specify from where we want string with jumpindex
# list=[start:end:jumpIndex]
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])  # using positive indexes-[3,6]
print(animals[-7:-2])  # using negative indexes-[-7,-3]
print(animals[-8:-1:2])	#using negative indexes-[-8,-2,2]

