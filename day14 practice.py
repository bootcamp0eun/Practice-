# 10.1
class Thing:
    pass


print(Thing)
example = Thing()
print(example)


# 10.2
class Thing2:
    letters = 'abc'


print(Thing2.letters)


# 10.3
class Thing3:
    def __init__(self):
        self.letters = 'xyz'


home = Thing3()
print(home.letters)


# 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


make = Element("Hydrogen", "H", 1)


# 10.5
el_dict = {"name": "Hydrogen",
           "symbol": "H",
           "number": 1}
hydrogen = Element(el_dict["name"], el_dict["symbol"], el_dict["number"])
