class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "x = %d, y = %d"%(self.x, self.y)

    def add(self):
        return self.x + self.y


maths = []

maths.append( Math(2,3) )
maths.append( Math(12, 4) )
maths.append( Math(222,5) )
maths.append( Math(12,6) )

tempMath = Math(42, 5)
maths.append(tempMath)

for math in maths:
    print math
    print math.add()

print maths[0].add()

myTempMath = maths[0]
print myTempMath.add()








