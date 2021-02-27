class Animal(object):  # when we are adding object to a class, it leads to have all the magic function in the class which is Parent class
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):  # inherite from Animal class

    def walk(self):
        print('walk')


class Fish(Animal):

    def swim(self):
        print('swim')


m = Mammal()
m.eat()
print(m.age)

print(isinstance(m, Animal))
print(isinstance(m, Mammal))
print(issubclass(Mammal, Animal))
