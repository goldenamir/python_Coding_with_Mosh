class Point:
    default_colot = 'red'  # it is an example of class attribute

    def __init__(self, x, y):  # x and y are attributes in Point class
        self.x = x
        self.y = y

    @classmethod  # is a decorator
    def zero(cls):  # cls is shortten for class
        return cls(0, 0)

    def draw(self):  # is a method of Poing class
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()  # method in class level
point.draw()
