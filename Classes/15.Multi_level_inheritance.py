class Animal:
    def eat(self):
        print('eat')


class Bird(Animal):
    def fly(self):
        print('fly')


class Chicken(bird):
    pass


# it is better to eliminate the multi-level inheritance
