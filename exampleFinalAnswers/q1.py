
class BarTab:
    def __init__(self, name):
        names = name.split()
        # just the first name
        self.name = names[0]
        self.balance = 0.0

    def getTab(self):
        return self.balance

    def makePayment(self, amount):
        if amount > self.balance:
            self.balance = 0
        else:
            self.balance -= amount

    def addToTab(self, amount):
        self.balance += amount

    def __str__(self):
        return "%s has a balance of %d"%(self.name, self.balance)

# tests (you do not have to do this on the final)
joe = BarTab("Joe Fred Billy-Bob Clampett")
print(joe)

joe.addToTab(10)
joe.addToTab(40)
print(joe)

joe.makePayment(100)
print(joe)