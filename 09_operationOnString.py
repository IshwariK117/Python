# find length of a string using length method
language = 'python'
print(len(language))

# string as an array
pie = "ApplePie"
print(pie[2:])  # slicing till the end
print(pie[:5])  # slicing from the start
print(pie[6])  # index at position 6
print(pie[2:-3])  # slicing in between
print(pie[:])  # whole string displayed
print(pie[3:7:2])  # slicing in between by moving 2 positions
print(pie[::-1])  # reverse the string

print(pie.upper())
print(pie.lower())

# Corrected startsWith and endsWith methods
print(pie.startswith('appy'))  # Check if pie starts with 'appy'
print(pie.endswith('Pie'))  # Check if pie ends with 'pie'

fruit = 'Litchi'
print(fruit.index('i'))  # index of 'i' from the beginning
print(fruit.count('i'))  # count occurrences of 'i'

# loop through alphabet
alphabet = 'ABCDE'
for i in alphabet:
    print(i)
