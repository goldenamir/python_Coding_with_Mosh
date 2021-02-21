class Point:
    default_colot = 'red'  # it is an example of class attribute

    def __init__(self, x, y):  # x and y are attributes in Point class
        self.x = x
        self.y = y

    def draw(self):  # is a method of Poing class
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(Point.default_colot)  # I am calling class attribute
print(point.default_colot)  # I am calling instance attribute
point.z = 10  # we can attribute out of the class like 'z'
point.draw()


another = Point(3, 4)  # 3 and 4 are attributes of the instance
another.draw()
