class Animal:
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

# In the below two classes we have to function which are same so we can use ' inheritance ' for handling the issue
# class Mammal:
#     def eat(self):
#         print('eat')

#     def walk(self):
#         print('walk')


# class Fish:
#     def eat(self):
#         print('eat')

#     def swim(self):
#         print('swim')
