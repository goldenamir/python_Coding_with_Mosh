'''class Product:

    def __init(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError('price cannot be negative.')
        self.__price = value

    price = property(get_price, set_price)



'''
# the above mentioned method is more noisy for giving a property
# in below we can use more clear method which is 'decorator'


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative value.')
        self.__price = value


product = Product(10)
product.price = -1
print(product.price)
