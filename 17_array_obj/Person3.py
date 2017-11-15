
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def __str__(self):
        return self.firstname + " " + self.lastname + " is " + str(self.age)
    
    # instance method
    def addToAge(self):
        self.age += 1
        

maggie = Person('Maggie', 'Simpson', 1)
lisa = Person('Lisa', 'Simpson', 9)
bart = Person('Bart', 'Simpson', 12)


print maggie

# it's maggie's birthday
maggie.addToAge()
print maggie


















