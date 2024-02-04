# isdisjoint():checks if items of given set are present in another set ,return false if items are present
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo",  "Madrid"}
print(cities.isdisjoint(cities2)) #output:False

#issuperset():return true if all items present in another set
print(cities.issuperset(cities2))  #output:True

#issubset():checks if all the items of the original set are present in the particular set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

