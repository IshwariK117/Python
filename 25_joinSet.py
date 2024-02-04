# we can perform operation like union or intersect just like mathematics

# union() and update() method print all items that are present in two sets
# the union method return new sets whereas update method add item in existing set

days1 = {"Sun", "Mon", "Tues", "wednes"}
days2 = {"Thurs", "Wednes", "Fri", "Sat"}
days3 = days1.union(days2)
print(days3)  # output:{'Sun', 'Fri', 'Thurs', 'Mon', 'Tues', 'Wednes', 'wednes', 'Sat'}

days1.update(days2)
print(days1)  # output:{'Sun', 'Fri', 'Thurs', 'Mon', 'Tues', 'Wednes', 'wednes', 'Sat'}

# intersection() -add items in new set which are same in  both sets
season1 = {"summer", "Mansoon", "Winter", "Spring"}
season2 = {"Autumn", "Winter", "Spring", "hemant", "shishir"}
days4 = season1.intersection(season2)
print(days4)  # output:{'Spring', 'Winter'}

# symmetric_differnce()-return the items which are not similar in both sets
days5 = season1.symmetric_difference(season2)
print(days5)  # output:{'shishir', 'hemant', 'Mansoon', 'summer', 'Autumn'}

# difference():prints items which only in original list
days6=season1.difference(season2)
print(days6) #output:{'summer', 'Mansoon'}
