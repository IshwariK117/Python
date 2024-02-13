# while :execute the statement while the condition is true when it becomes false come out of the loop
count = 5
while (count <= 10):
    print(count)
    count += 1
print("------------------------")
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print(" counter 0")
print("------------------------")
'''
for loop-
iterate over a sequnce of iterable object,means iterating over list,tuple,set,dictionary
'''
name = "ishwari"
for i in name:
    print(i)
print("-------------------------")
colors = ("Red", "Green", "Blue", "Yellow")
for x in colors:
    print(x)

print("-------------------------")
for k in range(5):
    print(k)

print("--------------------------")
'''
nested loop-
loop inside loop
'''

i = 2
while (i <= 2):
    for k in range(1, 11):
        print(i, "*", k, "=", (i*k))
    i = i + 1
    print()

print("---------------------------")
for i in range(1, 4):
    k = 1
    while (k<=3):
        print(i, "*", k, "=", (i*k))
        k = k + 1
    print()