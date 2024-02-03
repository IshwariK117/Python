# Tuple Indexes
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]

#positive indexing:
print(country[1])
print(country[3])
print(country[0])

#negative indexing:
print(country[-1])
print(country[-3])
print(country[-4])

#we can check if the given item is present or not
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")


