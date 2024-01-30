str1 = "Hey ,Shrek"
str2 = "How are you?"
print(str1 + str2)  # concatenate two string

str3 = 'hello'
age = 19
# print(str3 + age)  # concatenate of string and integer not allowed ---  #typeError

# We make the use of format() method. The format() methods places the arguments within the string wherever the placeholders are specified.
name = "Ishwari kape"
age = 20
statement = "My name is {} and my age is {}."
print(statement.format(name, age))

# we can also make use of indexes to place the argument in specified order
quantity = 2
fruit = "Apples"
cost = 90.0
stmt = "I want to buy {0} {1} and the cost is {2}"
print(stmt.format(quantity, fruit, cost))