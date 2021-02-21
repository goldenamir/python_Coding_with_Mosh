class Point:

    def __init__(self, x, y):  # x and y are attributes in Point class
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):  # is a method of Poing class
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)  # instance of the class
print(point)
