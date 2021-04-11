# creating a point class
# for naming in class we use Pascal naminig convention
class Point:
    def draw(self):
        print('draw')


point = Point()
print(type(point))
# checking point is an instance in class which is called 'Point' and the result will be Flase or True
print(isinstance(point, Point))
print(isinstance(point, int)) # result will be Flase 