## set extend python
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print("union :", A | B)

print("intersection :", A | B)

# elements not present both sets

print("Symmetric difference :", A ^ B)   
#Symmetric difference : {0, 1, 3, 5, 6, 8}

#adding two or more elements in a list
list1 = [1,2,3,4,5]
list1.extend([6,7,8])
print(list1)
#output = [1, 2, 3 ,4 ,5, 6, 7, 8]

# https://www.codegrepper.com/code-examples/python/extend+in+list+python
#extend in list python
subjects=["Maths","Science","Arts","Commerce"]
subjects_2=["Artificial intelligence","Statistics"]
subjects.extend(subjects_2)
print(subjects)  ## used to add more elements from other list

# https://www.codegrepper.com/code-examples/python/a+list+inside+a+list+python

# a list inside a list python
listName = [1,2,3,4]
board = []    
for i in range(6): # create a list with nested lists
    board.append([])
    for n in range(6):
        board[i].append("O") # fills nested lists with data

#https://www.codegrepper.com/code-examples/python/python+nested+list+comprehension
#python nested list comprehension
# 2-D List 
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
  
# Nested List Comprehension to flatten a given 2-D matrix 
flatten_matrix = [val for sublist in matrix for val in sublist] 
  
print(flatten_matrix)
# https://www.codegrepper.com/code-examples/python/python+nested+list+comprehension
#nested loop in list comprehension 
matrix = [[j for j in range(5)] for i in range(5)]

#https://www.codegrepper.com/code-examples/python/python+nested+list
#python nested list

# example of a nested list
my_list = [[1, 2], ["one", "two"]]

# accessing a nested list
my_list[1][0] # outputs "one"

#how to make one list from nested list 

from collections import Iterable
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

lis = [1,[2,2,2],4]
list(flatten(lis))
[1, 2, 2, 2, 4]
list(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
[1, 2, 3, 4, 5, 6, 7, 8, 9]


#python nested list 

L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]   
for list in L:
    for number in list:
        print(number, end=' ')
# Prints 1 2 3 4 5 6 7 8 9


https://www.codegrepper.com/code-examples/python/python+how+to+unnest+a+nested+list
#python how to unnest a nested list”

# Basic syntax:
unnested_list = list(chain(*nested_list))
# Where chain comes from the itertools package and is useful for 
#	unnesting any iterables

# Example usage:
from itertools import chain
nested_list = [[1,2], [3,4]]
my_unnested_list = list(chain(*nested_list))
print(my_unnested_list)
[1, 2, 3, 4]

https://www.codegrepper.com/code-examples/python/python+flatten+list
#python flatten list
flat_list = [item for sublist in l for item in sublist]

#which is equivalent to this 
flat_list = []
for sublist in l:
    for item in sublist:
        flat_list.append(item)

# idiomatic python

# using itertools
import itertools

list_of_list = [[1, 2, 3], [4, 5], [6]]
chain = itertools.chain(*images)

flattened_list = list(chain)
# [1, 2, 3, 4, 5, 6]


#flatten a list of lists python 
flattened = [val for sublist in list_of_lists for val in sublist]
#flatten a list of lists python 
flat_list = [item for sublist in t for item in sublist]

#flatten a list of lists python 
itertools.chain.from_iterable(factors)
#flatten a list of lists python 
flat_list = []
for sublist in l:
    for item in sublist:
        flat_list.append(item)

https://www.codegrepper.com/code-examples/python/python+flat+list+from+list+of+list

#python flat list from list of list

flat_list = [item for sublist in l for item in sublist]

#which is equivalent to this 
flat_list = []
for sublist in l:
    for item in sublist:
        flat_list.append(item)


# idiomatic python

# using itertools
import itertools

list_of_list = [[1, 2, 3], [4, 5], [6]]
chain = itertools.chain(*images)

flattened_list = list(chain)
# [1, 2, 3, 4, 5, 6]


flat_list = []
for sublist in l:
    for item in sublist:
        flat_list.append(item)

#python every other goes to a list
import numpy as np
values=np.arange(0,10)
print(values[::2])

a = [1, 2, 3, 4, 5]
a[1::2]
# returns 2, 4
a[::2]
#returns 1, 3, 5

def altElement(a):
    return a[::2]

#python convert nested list to list of strings” Code Answer
# Basix syntax:
['delim'.join([str(elem) for elem in sublist]) for sublist in my_list]
# Where delim is the delimiter that will separate the elements of the
#	nested lists when they are flattened to a list of strings

# Note, this uses two "levels" of list comprehension

# Example usage 1:
my_list = [[1, '1', 1], [2,'2',2], [3,'3',3]]
[' '.join([str(elem) for elem in sublist]) for sublist in my_list]
##--> ['1 1 1', '2 2 2', '3 3 3'] # List of space-delimited strings

# Example usage 2:
my_list = [[1, '1', 1], [2,'2',2], [3,'3',3]]
['_'.join([str(elem) for elem in sublist]) for sublist in my_list]
##--> ['1_1_1', '2_2_2', '3_3_3'] # List of underscore-delimited strings


#python check list contains another list
https://www.codegrepper.com/code-examples/python/python+check+list+contains+another+list

## checking any elment of list_B in list_A
list_A = [1, 2, 3, 4]

list_B = [2, 3, 6]

check = any(item in list_A for item in list_B)

print(check)
# True

'''    
    check if list1 contains any elements of list2
'''
result =  any(elem in list1  for elem in list2)
if result:
    print("Yes, list1 contains any elements of list2")    
else :
    print("No, list1 contains any elements of list2")

#>>> items = set([-1, 0, 1, 2])
#>>> set([1, 2]).issubset(items)
#True
#>>> set([1, 3]).issubset(items)
#False


## using set
list_A = [1, 2, 3, 4]
list_B = [2, 3]

set_A = set(list_A)
set_B = set(list_B)

print(set_A.intersection(set_B))

# True if there is any element same
# False if there is no element same

#python check if list contains elements of another list” Code Answer’s
## checking any elment of list_B in list_A
list_A = [1, 2, 3, 4]

list_B = [2, 3, 6]

check = any(item in list_A for item in list_B)

print(check)
# True

## checking all elements of list_B in list_A
list_A = [1, 2, 3, 4]
list_B = [2, 3]

check = all(item in list_A for item in list_B)

print(check)
# True

'''    
    ##check if list1 contains any elements of list2
'''
result =  any(elem in list1  for elem in list2)
if result:
    print("Yes, list1 contains any elements of list2")    
else :
    print("No, list1 contains any elements of list2")

#>>> items = set([-1, 0, 1, 2])
#>>> set([1, 2]).issubset(items)
#True
#>>> set([1, 3]).issubset(items)
#False


## using set
list_A = [1, 2, 3, 4]
list_B = [2, 3]

set_A = set(list_A)
set_B = set(list_B)

print(set_A.intersection(set_B))

# True if there is any element same
# False if there is no element same

