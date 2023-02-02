# 10.8
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    @property
    def get_name(self):
        return self.name

    @property
    def get_symbol(self):
        return self.symbol

    @property
    def get_number(self):
        return self.number


el_dict = {"name": "Hydrogen",
           "symbol": "H",
           "number": 1}
hydrogen = Element(el_dict["name"], el_dict["symbol"], el_dict["number"])