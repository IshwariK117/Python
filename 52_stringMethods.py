# capitalize()-converts first charcater to uppercase,and rest is lowercase
txt = "hello and welcome to my world"
print(txt.capitalize())  # Hello and welcome to my world

txt = "python is FUN!"
x = txt.capitalize()
print(x)  # Python is fun!

# center()-it will center allign the string by a specific charachter
# string.center(length, character)
text = "Banana"
print(text.center(40, "-"))  # -----------------Banana-----------------

# count()-return number of times specified value appears in string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# endswith() -return true if string ends with specified value,otherwise false
x = txt.endswith("Fruit")
print(x)

# find()-find the first occurence of specified value , return -1 if not found
print(txt.find("e"))
print(txt.find("e", 6, 19))

# format()-format the specified  value and insert them inside string placeholder
txt = "for only {price:.2f} dollars"
print(txt.format(price=49))

x = "my name is {} ,i am {} years old".format("ishwari", 20)
print(x)

x = "my name is {0} ,i am {1} years old".format("ishwari", 20)
print(x)

# index()-find the first occurrence of specified value
print(txt.index('o'))

# isalnum()-return true if all characters in text are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)  # True

# isalpha()-returns true if all characters are alphabet letters
x = txt.isalpha()
print(x)  # False

# isascii()-returns true if all characters are ascii characters
x = txt.isascii()
print(x)

# isdigit()-return true if all characters in string are number
a = "\u0030"  # unicode for 0
b = "\u00B2"  # unicode for ²

print(a.isdigit())
print(b.isdigit())

# islower()-returns tue if all chatracters are in lowercasess
txt = "hello world!"
x = txt.islower()
print(x)

# isupper()-returns true if all chatracters are in uppercase
txt = "Hello World!"
x = txt.isupper()
print(x)

# join()- method takes all items in an iterable and joins them into one string.
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# lstrip()-removes any leading character
txt = "          banana"
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

# partition()-method searches for a specified string, and splits the string into a tuple containing three elements
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# replace()-this method replace specified phrase with another phrase
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)

# rfind()- method finds the last occurrence of the specified value.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

#rstrip()- method removes any trailing characters (characters at the end a string)
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

#swapcase()-method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#translate()- method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))