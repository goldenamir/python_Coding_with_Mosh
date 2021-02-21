point = {'x': 1, 'y': 2}
# we can use dict() function for creating dictionary

point = dict(x=1, y=2)  # it is more easier for handling

print(point['x'])
print(point)
point['z'] = 20
print(point)

if 'a' in point:
    print(point['a'])

print(point.get('a', 0))  # if a is not exist in point return 0 by default

del point['x']  # deleting an item from a dictionary
print(point)

# this iteration gives us all the keys in the dict
for x in point:
    print(x)

# for iterating on the dict and have all the key and its values
for key in point:
    print(key, point[key])

# an other better way to iterate on a dictionary
for x in point.items():
    print(x)


'''
# Dictionary comprehensions:
'''
values = []
for x in range(5):
    values.append(x*2)

# expression in List
# [expression for item in items]
values = [x*2 for x in range(5)]
print(values)

# in the set we have just have values but in the dictionaries we have keys and values
# comprehension which cause to create a set as below
values = {x*2 for i in range(5)}  # so this is set which has a values only

# comprehension which causes to create a dictionary as below
values = {x: x*2 for x in range(5)}  # now we have keys and values
