################################################

#Tuples
# tuples are immuatble, useful for fixed data,faster than List, Sequence time.
# A tuple is a sequence of immutable Python objects. Tuples are
# sequences, just like lists. The differences between tuples
# and lists are, the tuples cannot be changed unlike lists and
# tuples use parentheses, whereas lists use square brackets.
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = "a", "b", "c", "d"
###########################################

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)      # dog
###################################################