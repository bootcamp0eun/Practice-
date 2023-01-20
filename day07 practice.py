print("Chapter 10. practice\n")

# 10.1
print("# 10.1")
class Thing:
    pass


print(Thing())
example = Thing()
print(example)
print('-> 두 출력값이 같다!')



# 10.2
print('\n# 10.2')
class Thing2:
    pass


Thing2.letters = 'abc'
print(Thing2.letters)


# 10.3
print('\n# 10.3')
class Thing3:
    def __init__(self):
        self.letters = 'xyz'


t3 = Thing3()
print(t3.letters)
print('-> yes(maybe..)')


# 10.4
print('\n# 10.4')
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


a = Element('Hydrogen', 'H', '1')


# 10.5
print('\n# 10.5')
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
