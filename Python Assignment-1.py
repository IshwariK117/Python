'''
Problem Description: You are given a list of students with their names, ages, and grades. Your task is to process this data and perform the following operations:
1. Calculate the average age of all the students.
2. Determine the student with the highest grade.
3. Create a dictionary where the keys are the student names and the values are their ages.
4. Convert the student data into a set of tuples, where each tuple contains the name, age, and grade of a student.
5. Sort the student data based on their grades in descending order.

'''

students = [
    {"name": "Alice", "age": 20, "grade": 85.5},
    {"name": "Bob", "age": 19, "grade": 92.3},
    {"name": "Charlie", "age": 21, "grade": 89.1},
    {"name": "David", "age": 18, "grade": 95.7}
]

# 1. Calculate the average age of all the students.
total_age = 0
for student in students:
    total_age = total_age + student["age"]

average = total_age / len(students)
print(average)  # output:19.5

# 2.Determine the student with the highest grade.
for grade in students:
    maxGrade = max(students, key=lambda s: s["grade"])
print(maxGrade["name"])  # output:David

# 3.Create a dictionary where the keys are the student names and the values are their ages.
stud_dict = {}
for stud in students:
    stud_dict[stud["name"]] = stud["age"]
print(stud_dict)  # output:{'Alice': 20, 'Bob': 19, 'Charlie': 21, 'David': 18}


# 4.Sort the student data based on their grades in descending order.
def my_func(e):
    return e['grade']

students.sort(key=my_func, reverse=True)
print(
    students)  # output:[{'name': 'David', 'age': 18, 'grade': 95.7}, {'name': 'Bob', 'age': 19, 'grade': 92.3}, {'name': 'Charlie', 'age': 21, 'grade': 89.1}, {'name': 'Alice', 'age': 20, 'grade': 85.5}]


# 5.Convert the student data into a set of tuples.
stud_data = ()
for stud in students:
    current_tuple = (stud["name"], stud["age"], stud["grade"])
    print(current_tuple)

'''
output:('David', 18, 95.7)
('Bob', 19, 92.3)
('Charlie', 21, 89.1)
('Alice', 20, 85.5)
'''
