# add():we can add items uisng this method
states = {"delhi", "gujrat", "maharashtra", "tamilndu", "M.P"}
print(states)

states.add("rajsthan")
print(states)

# if we want to add more than one item or set of items ,we just have to use update() method
states2 = {"kerala", "UP", "sikkim"}
states.update(states2)
print(states)

# remove()-remove item from set
states.remove("UP")
print(states)

# discard():same as remove method ,removes item from set
states.discard("kerala")
print(states)

# pop(),clear(),del:
print(states.pop())

print(states.clear())  #clear all items

del states2
#print(states2)    #del is keyword that delete all iems







