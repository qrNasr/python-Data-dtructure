# Key/Value pairs
# Associate array , like javaHashMap
# Dict are unordered.

x = {'fish':25.3,'beef':33.8, 'chicken': 22.7} 
print(x)
#other way to create a dictionary by passing a tuple of a list proceeded by a dict word.

y = dict([('fish',25.3),('beef',33.8), ('chicken', 22.7)])
print(y)

k = dict(fish=25.3,beef = 33.8,chicken= 22.7)
print(k)

# to add an item to a dict
x['shrimp']=38.2 # add or update if not listed.
del(x['shrimp'])

# get a lenght of a dictionary

print(len(x))
x.clear() 
#delete dict x
del(x)

# access keys and values in a Dict.

x ={'fish':25.3,'beef':33.8, 'chicken': 22.7}
print(x.keys())
print(x.values())
print(x.items())

## check a membership of only keys.
print('beef' in x )

## check a membership of only values.
print('beef' in x.values())

