""" Tuples """"

# is a read only list
point = 1,  # since it has a comma so it is tuple for Python
point = 1, 2
print(type(point))  # python will see it as tuple

point = (1, 2) + (3, 4)  # will concatenate two tuples
point = tuple([2, 2])
point = tuple(" Hello World!")
print(point[0:2])  # indexing of tuple

if 10 in point:
    print('exists')

""" swaping variables """
x = 10
y = 11

z = x
x = y
y = z
print('x', x)

# better way
x, y = y,
