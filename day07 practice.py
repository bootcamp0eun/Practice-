# 10.6
print('# 10.6')
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'{self.name}, {self.symbol}, {self.number}')


hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()
