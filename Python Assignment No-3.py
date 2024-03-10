'''

Lists 
1. Write a funcon that takes a list of numbers as input and returns the sum of the even numbers in the list. 
2. Write a funcon that takes a list of words as input and returns the longest word in the list.
3. Write a funcon that takes a list of characters as input and removes all duplicate characters from the list. 
4. Write a program that takes a list of numbers as input and sorts the list in ascending order.
5. Write a program that takes a list of words as input and reverses the order of the words in the list. 
'''


# 1.Write a funcon that takes a list of numbers as input and returns the sum of the even numbers in the list.
def sum_of_evens(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total


list1 = [1, 3, 4, 5, 2]
print(sum_of_evens(list1))


# 2. Write a funcon that takes a list of words as input and returns the longest word in the list.
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# Example usage:
word_list = ["apple", "banana", "orange", "strawberry"]
print(longest_word(word_list))


# 3. Write a funcon that takes a list of characters as input and removes all duplicate characters from the list.
def remove_duplicates(characters):
    unique_chars = []
    seen = set()  # Keep track of seen characters
    for char in characters:
        if char not in seen:
            unique_chars.append(char)
            seen.add(char)
    return unique_chars


# Example usage:
char_list = ['a', 'b', 'c', 'b', 'a', 'd', 'e']
print(remove_duplicates(char_list))


# 4. Write a program that takes a list of numbers as input and sorts the list in ascending order.
def sort_numbers(numbers):
    return sorted(numbers)


# Example usage:
numbers_list = [4, 2, 7, 1, 5]
sorted_numbers = sort_numbers(numbers_list)
print(sorted_numbers)


# 5. Write a program that takes a list of words as input and reverses the order of the words in the list.
def reverse_words(words):
    return words[::-1]


# Example usage:
words_list = ["apple", "banana", "orange", "strawberry"]
reversed_words = reverse_words(words_list)
print(reversed_words)
