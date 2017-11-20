class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        try:
            self.x = float(x)
        except:
            print "Can't do it"

    def add(self):
        return self.x + self.y



firstMath = Math(2, 6)

firstMath.setX(3)
print firstMath.add()

firstMath.setX("meow")
