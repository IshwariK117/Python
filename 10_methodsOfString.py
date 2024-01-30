# upper():converts string to uppercase
str1 = "Hello,This is Ishwari kape"
print(str1.upper())

# lower():converts string to lowercase
print(str1.lower())

# strip():remove the whitespaces before and after the string
str2 = " Python string methods "
print(str2)
print(str2.strip())

# rstrip(): removes any trailing characters
str3 = "Hello #!!!"
print(str3.rstrip("!"))

# replace():replace the string by another string
str4 = "The Group"
print(str4.replace("Gr", "S"))

# split():split the string into separate strings
print(str4.split())

# capitalize(): it turns out first charachter of string Capital and rest out into the lowercase ,it does not have any effect if t is capitalize already
str5 = "python "
print(str5.capitalize())
str6 = "hello WorlD"  # it will convert rest of character into lowercase
print(str6.capitalize())

# center(): align given string to center as per parameter
print(str6.center(50, "."))

# count():count the number of occurrences of charcter
print(str6.count("o"))

# startswith():check if the string starts with given value
str7 = "Welcome to the Console !!!"
print(str7.startswith("Wel"))

# endswith():check if the string ends with given value
print(str7.endswith("!"))

# find(): searches for the first occurrence of string and returns the -1 if not found
str8 = "He's name is John. He is an honest man."
print(str8.find("is"))
print(str8.find("hi"))  # return -1

# index():serches for first occurrence of string and raise an exception if not found
print(str8.index("is"))
# print(str8.index("hi"))  # raise an ValueError

# isalnum() : The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

# islower() : The islower() method returns True if all the characters in the string are lower case, else it returns False.
str1 = "hello world"
print(str1.islower())

# isspace() : The isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "        "  # using Spacebar
print(str1.isspace())
str2 = "        "  # using Tab
print(str2.isspace())

# istitle() : The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str1 = "World Health Organization"
print(str1.istitle())

# isupper() : The isupper() method returns True if all the characters in the string are upper case, else it returns False.
str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())


