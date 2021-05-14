# indexing
# indexing - means access any item in the sequence using it's index.
# string indexing
x= 'frog'
print(x[3])
# lis indexing
x =['cat','cow','horse']
print(x[1])
# Tuple indexing
x = ('kevin','Niklas','jenny','craig')
print(x[1])
# slicing
# slicing out substring , sublist, subtuples, using index
# [start:end+1:step]
k = 'computer'
print(k[1:4])
print(k[1:6:2])
print(k[3:])
print(k[:5])
print(k[-1])
print(k[-3:])
print(k[:-2])
## adding / concatenating 
x= 'horse'+'shoe'
print(x)
# concatenating  lists
y = ['cat','cow']+ ['horse']
print(y)
# concatenating tuples
z = ('kevin','niklas','jenny') +('craig',)
# you have to add a comma at the end so that it will be considered a tuple
print(z)
# Multiply a sequence 
# string
x = 'bug'*3
print(x)
# list
y= [8,5] *3
print(y)
# tuple 
z = (2,4)*3
print(z)

# check boolean
# String
x= 'bug'
print('u' in x)
#list
y=['cat','cow','horse']
print('cow' in y)
# tuple
z= ('kevin','Niklas','jenny','craig')
print('niklas' in z)

# Iteration

#item
x= [7,8,9]
for item in x:
    print(item)

# index and item
y= [7,8,9]
for index , item in enumerate(y): # you have to write in enumerate
    print(index,item)

L = [7,8,9]
for index , item in enumerate(L):
    print(item,index)

# count the number of items in a sequence

# string
x= 'bug'
print(len(x))

#list
y=['cat','cow','horse']
print(len(y))

#tuple
z= ('kevin','Niklas','jenny','craig')
print(len(z))

## Minimum - Find the minimum item in a sequence lexicographically.
# Alpha or numeric types, but can't be mix types.

x= 'bug'
print(min(x))
#list
y=['cat','cow','horse']
print(min(y))
# tuple
z= ('kevin','Niklas','jenny','craig')
print(min(z))

## Maximum - Find the minimum item in a sequence lexicographically.
# Alpha or numeric types, but can't be mix types.
x= 'bug'
print(max(x))
#list
y=['cat','cow','horse']
print(max(y))
# tuple
z= ('kevin','Niklas','jenny','craig')
print(max(z))

## Sum - find the sum of items in a sequence.
## Entire sequence must be numeric

# list
y = [2,5,8,12]
print(sum(y))
print(sum(y[-2:]))

# tuple
z = (50,4,7,19)
print(sum(z))

# Sorting - returns a new list of items in sorted order.
#Does not change the original list.
x= 'bug'
print(sorted(x))
#list
y=['cat','cow','horse']
print(sorted(y))
# tuple
z= ('Kevin','Niklas','Jenny','Craig') # small and capital letter matter
print(sorted(z))
# add a key parameter and lamba function to return second char.
# the word key is a defined parameter name, k is an arbitrary variable name.
z= ('Kevin','Niklas','Jenny','Craig') 
print(sorted(z,key=lambda k: k[1]))

## counting (items) - return count of an item
x= 'hippo'
print(x.count('p'))

#list
y=['cat','cow','horse','cow']
print(y.count('cow'))

# tuple
z= ('Kevin','Niklas','Jenny','Craig') 
print(z.count('Kevin'))

#index (item) - return the index of the first occurance of an item.
#string
x= 'hippo'
print(x.index('p'))

#list

y=['cat','cow','horse','cow']
print(y.index('cow'))

# tuple

z= ('Kevin','Niklas','Jenny','Craig') 
print(z.index('Jenny'))

## unpacking an item of a sequence into n variable

x = ['cat','cow','horse']
a,b,c = x
print(a,b,c)

##################################################

#lists

# General purpose
# Most widely used data structure
# Grow and shrink size as needed.
# Sequence type
#Sortable

# Constructor - creating a new list
x = list()
y = ['a',25,'dog',8,43]
tuple1 = (10,20)
z= list(tuple1)
print(z)

## List comprehension // read more about it.
a=[m for m in range(8)]
print(a)

b= [i**2 for i in range(10) if i>4]
print(b)

## delet item from a list

x= [5,3,8,6]
del(x[1])
print(x)
del(x)

## Append an item to a list
x= [5,3,8,6]
x.append(7)
print(x)

## extend - append a sequence to a list
x= [5,3,8,6]
y= [12,13]
x.extend(y)
print(x)

## insert - insert an item at a given index.
x= [5,3,8,6]
x.insert(1, 'nasr')
print(x)

## pop function

x= [5,3,8,6] # will remove last added item.
x.pop()
print(x)

# remove function - easy
# reverse function - easy

x= [5,3,8,6]
x.sort()
print(x)

# reverse sort - sort items descending.
# use reverse = True paramaeter to the sort function.

x= [5,3,8,6]
x.sort(reverse = True)
print(x)


# To access values in tuple, use the square brackets for
# slicing along with the index or indices to obtain value
# available at that index.
tup1[0] # Output: 'physics'

# Constructor - creating a new tuple

x = () # empty tuple
x = (1,2,3)
x = 1,2,3
x = 2, # if no comma, no tuple
print(x,type(x))

x = (1,2,3,4)
#del(x[1]) # false
#x[1]= 8   # false

y = ([1,2],3) # a tuple where the first item is a list
del(y[0][1])  # delete the 2
print(y)      # the list within the tuple is mutable

y +=(4,)      # concatenating two tuples works
print(y)

####################################

##Sets#####
# store non-duplicate values
# very fast access vs lists
# math Set ops (union,intersect)
# Sets are unordered.
#constructor - Creating new sets

x = {3,5,3,5}
y = { 900,100,120}
print(x)

y= set()
print(y)

list2 = [2,3,4]
z = set(list2)
print(z)

## set operations
x= {3,4,6}
y = { 900,100,120}
print(x)
x.add(100) # add item
print(x)
x.remove(4) # remove item
print(x)
print(5 in x) # check membership
print(x.pop(),x)
x.clear()
print(x.difference(y))
x.difference(y) # output {3, 4, 12, 6}
print(x)
x.discard(2)
print(x)
x.extend()
#x.insert()
#x.append(y)
#print(x)
#x.extend(y)

## math operation on Sets

#intersection (AND) Set1 & Set2
# union (OR) :Set | set 2

s1 = {1,2,3,4}
s2 = {3,4,5}
print(s1 & s2)
print(s1|s2)
print(s1^s1)
print(s1-s1)
print(s1<=s1)
print(s1>=s1)


