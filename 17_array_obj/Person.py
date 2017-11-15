
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 10
        

maggie = Person('Maggie')
lisa = Person('Lisa')
bart = Person('Bart')


print maggie.name
print bart.name


bart.name = 'Barthalemu'
print bart.name
        
print bart.age