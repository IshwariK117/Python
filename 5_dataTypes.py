'''
 Data type refers the type of variable require
 1. numeric data type
 int:3,-4,5
 float:3.4,4.5,-9.000
 complex:6+2i

 2.String
 "Hello ,world",'Welcome '

 3.Boolean
 True,False

 4.Sequenced data type:list,tuple ,range
 list -list is ordered collection of data type enclosed in square brackets,which is mutable
 tuple -tuple is orderd collection enclosed in pathenthesis ,which is immutable
 range -return a sequenced of numbers specified by user starts by 0 ,increments by 1 by default

 5.Mapped data -dict
 unorderd collection of data containing key:value pair enclosed in curly braces

 6.set data type
 unorderd collection of element in which no element is repeated enclosed in curly braces
'''

int1 = 34
int2 = -23645
print(type(int1))
print(type(int2))
flt1 = 23.3
flt2 = 345E3
print(type(flt1))
print(type(flt2))
cmplx1 = 2 + 4j
cmplx2 = 6j
print(type(cmplx1))
print(type(cmplx2))

print("Hello,This is Ishwari kape")
print('from computer department')

list1 = [2, 3, [3, 4], 'hi']  # list
print(list1)

tuple1 = (4, 5, (3, 5), 'hello')  # tuple
print(tuple1)

for i in range(4, 10, 2):  # range
    print(i)

my_dict = {'name': 'sakshi', 'age': 20, 'canVote': True}  # dictionary
print(my_dict)

my_set = {1, 2, 3, 4, 5, 4}  # set
print(my_set)
