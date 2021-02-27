class Animal:
    def __init__(self):
        print('Animal constructor')
        self.age = 1

    def eat(self):
        def __init__(self):
            super().__init__()
            print('Mammal constructor')
            self.weight = 2
        print('eat')


class Mammal(Animal):
    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')
