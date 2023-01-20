# 10.8
print('# 10.8')
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)
