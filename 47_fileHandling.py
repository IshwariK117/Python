f = open("mydemo.txt")

f = open("mydemo.txt", "r")
print(f.read())

# Return the 5 first characters of the file:

f = open("mydemo.txt", "r")
print(f.read(3))

# Read one line of the file:

f = open("mydemo.txt", "r")
print(f.readline())

# Read two lines of the file:

f = open("mydemo.txt", "r")
print(f.readline())
print(f.readline())

# Loop through the file line by line:

f = open("mydemo.txt", "r")
for x in f:
    print(x)

# Close the file when you are finish with it:

f = open("mydemo.txt", "r")
print(f.readline())
f.close()
