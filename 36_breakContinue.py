# break enable to skip over the program and terminate the loop
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("--------------------")

for i in range(1, 11):
    if (i == 5):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)

print("---------------------------------------")

# continue statement skip the iteration and start executing very next condition
for i in [1, 2, 3, 6, 7, 10]:
    if i % 2 != 0:
        continue
    print(i)  # print even number from list

print("------------------")
i = 0
while True:
    print(i)
    i = i + 1
    if (i % 5 == 0):
        break
