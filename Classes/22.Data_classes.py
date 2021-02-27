''' In Python, Python check two variables by their location (memory place) not the value of them'''


from collections import namedtuple


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    ''' for handling the comparsion '''
# we are going to use magic functions

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


P1 = Point(1, 2)
P2 = Point(1, 2)

# the result of this comparing will be FALSE since the place of saving variables are different
print(P1 == P2)

''' but we can use the below mentioend method to check the comparsion '''

print(id(P1))  # 'id'function provides us the address of P1
print(id(P2))


print(P1 == P2)


Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print('p1.x: ', p1.x)
print(p1, p2)
