class House:
    def __init__(self):
        self.numDoors = 2
        self.numWindows = 5
        self.address = "OH DEAR WHERE AM I, REPLACE THIS"
    
    def __str__(self):
        return ("My house has " + str(self.numDoors) 
        + " door and " + str(self.numWindows) + " windows")

myHouse = House()

print myHouse


# Or......
print ("My house has " + str(myHouse.numDoors) 
     + " door and " + str(myHouse.numWindows) + " windows")
