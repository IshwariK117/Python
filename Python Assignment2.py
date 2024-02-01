'''
#1. list manipulation
a. Write a function that takes a list of numbers and returns the sum of all even numbers in the list.
b. Write a function that takes a list of words and returns a new list containing only the words that start with the leer 'A' or 'a'.
c. Write a function that takes a list of characters and counts the number of occurrences of each character in the list
'''

# a. Write a function that takes a list of numbers and returns the sum of all even numbers in the list.
result = 0


def my_func(n):
    for number in n:
        global result
        if number % 2 == 0:
            result = result + number
    return result


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = my_func(num)
print(res)  # output:30


# b. Write a function that takes a list of words and returns a new list containing only the words that start with the leer 'A' or 'a'.
def my_func(w):
    result = []
    for words in w:
        if words[0] == 'A' or words[0] == 'a':
            result.append(words)
    return result


words = ['cat', 'Apple', 'ant', 'Dog', 'And']
res = my_func(words)
print(res)  # output:['Apple', 'ant', 'And']

# c. Write a function that takes a list of characters and counts the number of occurrences of each character in the list
res = {}


def my_func(l1):
    for char in l1:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res


l1 = ['a', 'b', 'd', 'c', 'a', 'b', 'd']
result = my_func(l1)
print(result)  # output:{'a': 2, 'b': 2, 'd': 2, 'c': 1}

'''
2. List Searching and Filtering: 
a. Write a funcon that takes a list of numbers and returns the index of the ﬁrst occurrence of a speciﬁc target number in the list. 
b. Write a funcon that takes a list of words and returns a new list containing only the words that have a length greater than or equal to a speciﬁed threshold.
c. Write a funcon that takes a list of items and returns a new list containing only the items that sasfy a certain condion, such as being divisible by a speciﬁc number or having a speciﬁc property. 
'''


# a. Write a funcon that takes a list of numbers and returns the index of the ﬁrst occurrence of a speciﬁc target number in the list.
def my_func(l1, trgt):
    for index in range(len(l1)):
        if l1[index] == trgt:
            return index


l1 = [1, 2, 3, 2, 1, 3, 3]
target = 3
result = my_func(l1, target)
print(result)  # output:2


# b. Write a funcon that takes a list of words and returns a new list containing only the words that have a length greater than or equal to a speciﬁed threshold.
def my_func(word_list, ts):
    result = []
    for word in word_list:
        if len(word) >= ts:
            result.append(word)
    return result


words = ['apple', 'mango', 'orange', 'yellow', 'pink']
trs = 5
res = my_func(words, trs)
print(res)  # output:['apple', 'mango', 'orange', 'yellow']


# c. Write a funcon that takes a list of items and returns a new list containing only the items that sasfy a certain condion,
# such as being divisible by a speciﬁc number or having a speciﬁc property.
def my_func(number):
    result = []
    for nums in number:
        if nums % 2 == 0:
            result.append(nums)
    return result


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = my_func(num)
print(res)  # output:['apple', 'mango', 'orange', 'yellow']

'''
3. List Operations and Transformaons: 
a. Write a function that takes a list of numbers and reverses the order of the elements in the list.
b. Write a function that takes a list of characters and converts all uppercase characters to lowercase. 
c. Write a function that takes a list of mixed numbers (whole numbers and fracons) and converts them to decimal form. 4
'''


# a. Write a functon that takes a list of numbers and reverses the order of the elements in the list.

def rev_order(list_of_num):
    list_of_num.reverse()
    print(list_of_num)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rev_order(list)  # output:[9, 8, 7, 6, 5, 4, 3, 2, 1]


# b. Write a function that takes a list of characters and converts all uppercase characters to lowercase.

def my_func(l2):
    new_list = []
    for char in l2:
        new_list += char.upper()
    return new_list


l2 = ['a', 'b', 'd', 'c', 'a', 'b', 'd']
result = my_func(l2)
print(result)  # output:['A', 'B', 'D', 'C', 'A', 'B', 'D']


# c. Write a function that takes a list of mixed numbers (whole numbers and fracons) and converts them to decimal form.
def my_func(mixed_num):
    decimal_numbers = []
    for num in mixed_num:
        decimal_numbers.append(float(num))
    return decimal_numbers


l3 = [1, 2.3, 3, 4, 5.0, 5.7, 7]
result = my_func(l3)
print(result)  # output:[1.0, 2.3, 3.0, 4.0, 5.0, 5.7, 7.0]

