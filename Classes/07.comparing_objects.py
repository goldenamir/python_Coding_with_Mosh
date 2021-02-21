class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


point = Point(1, 2)
other = Point(1, 2)
# comparing the address of referncing in the memory, so we need a magic method for comparing to objects
print(point == other)
print(point < other)
print(Point > other)
