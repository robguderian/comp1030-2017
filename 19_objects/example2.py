class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "x = %d, y = %d"%(self.x, self.y)

    def add(self):
        return self.x + self.y
    
    # We have to assume that other is a Math object
    def isEqual(self, other):
        equal = False
        if self.x == other.x and self.y == other.y:
            equal = True
        return equal
        
        
a = 1
b = 2

if a == b:
    print "hey"
else:
    print "nope"

math1 = Math(1, 2)
math2 = Math(1, 2)

print math2

# comparing memory pointers
if math1 == math2:
    print "I have nothing clever here"
else:
    print "nope"    
    
    
# compare contents of math1 and math2
if math1.x == math2.x and math2.y == math1.y:
    print 'huzzah'
else:
    print "nope"
    
    
if math1.isEqual(math2):
    print "huzzah!!!!"
else:
    print "still nope"
    
    
    
    
    
    
    
    
    