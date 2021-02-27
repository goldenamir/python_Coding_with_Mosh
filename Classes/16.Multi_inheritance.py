class Employee():
    def greet(self):
        print('Employee Greet')


class Person():
    def greet(self):
        print('Employee Greet')


class Manager(Employee, Person):
    pass


manager = Manager()
Manager.greet()  # it get from base class which is 'Employee'

# We wanna abstract the methods in classes


class Flyer:
    def fly(self):
        pass


class Swimer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimer):
    pass
