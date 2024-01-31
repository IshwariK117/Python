# adding list items in python
# 1.insert():insert the list in specified index ,user just have to specify index number
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.insert(1, "magenta")
print(colors)  # output: ['Red', 'magenta', 'Green', 'Blue', 'Yellow', 'Green']

# 2.append():append the items at the end of list
colors.append("white")
print(colors)  # output:['Red', 'magenta', 'Green', 'Blue', 'Yellow', 'Green', 'white']

# extend():this will add entire list of items or set or dictionary in existing list
light_Colors = ["lightGrey", "skyblue", "lightpink"]
colors.extend(light_Colors)
print(colors)

#add tuple in list
cars1=["Hundai","maruti","lamborgini"]
cars2=[""]
