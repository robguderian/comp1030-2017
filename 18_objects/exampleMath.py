class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x + self.y
    
    # accessor
    def getX(self):
        return self.x
    
    # mutator
    def setX(self, newX):
        try:
            # make sure it's an int
            self.x = int(newX)
        except:
            print "NOPE"

# instantiate
myEquation = Math( 10 , 42)

print myEquation.add()

mathObj = Math(2, 4)
# update the X
mathObj.setX(100)
print mathObj.add()
mathObj.setX("I also like turtles")
print mathObj.add()
