'''
-A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
-RegEx can be used to check if a string contains the specified search pattern.
'''

#Python has a built-in package called re, which can be used to work with Regular Expressions.

import re
text='hello,python'
x=re.search("^h .*python$",text)
if x:
  print("YES! We have a match!")
else:
  print("No match")


'''
findall-Returns a list containing all matches
search-Returns a Match object if there is a match anywhere in the string
split-Returns a list where the string has been split at each match
sub-Replaces one or many matches with a string
'''

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.findall("ain", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

