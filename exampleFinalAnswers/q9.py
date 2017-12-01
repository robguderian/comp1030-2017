class NumberHolder:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setFirst(self, newFirst):
        try:
            self.first = int(newFirst)
        except:
            print("Could not set number")
    
    def setSecond(self, newSecond):
        try:
            self.second = int(newSecond)
        except:
            print("Could not set number")
    
    def isEqual(self, other):
        equal = False
        if self.first == other.first and self.second == other.second:
            equal = True
        return equal

    def __str__(self):
        return "Holding: " + str(self.first) + " " + str(self.second)


number1 = NumberHolder(10, 20)
number2 = NumberHolder(100, 200)

print(number1.isEqual(number2))

number2.setFirst('a')
print(number2)

number2.setFirst(10)
number2.setSecond(20)
print(number1.isEqual(number2))
