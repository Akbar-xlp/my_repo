class Private:
    def __init__(self, name, price=0):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


ob_1 = Private("Akbar", 5000)
print(ob_1.get_name())
ob_1.name = "Asan"
print(ob_1.name)
print(ob_1.get_name())
