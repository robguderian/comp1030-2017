class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def marry(self,newLastName):
        self.lastName = self.lastName + "-" + newLastName
    
    def __str__(self):
        return "Hello, my name is %s %s"%(self.firstName, self.lastName)

britta = Person("Britta", "Perry")
print(britta)

britta.marry("Winger")
print(britta)

britta.marry("Chang")
print(britta)
