# pop():this method removes the last item in the list if no index is provide,if index is there then it removed given item
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop()        #removes the last item of the list
print(colors)

colors.pop(1)       #removes item at index 1
print(colors)


#remove(): This method removes specific item from the list.
colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.remove("blue")
print(colors)

#del:del is not a method, rather it is a keyword which deletes item at specific from the list, or deletes the list entirely.


colors = ["voilet", "indigo", "blue", "green", "yellow"]
del colors[3]
print(colors)

colors = ["voilet", "indigo", "blue", "green", "yellow"]
del colors
#print(colors)         #output:['voilet', 'indigo', 'blue', 'yellow']


#clear():This method clears all items in the list and prints an empty list.

colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)                  #output:[]

