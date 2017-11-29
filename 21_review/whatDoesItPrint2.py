import math
# also, what edge-cases are not dealt with?
class SomeObject:
    def __init__(self, content):
        self.content = content

    def doTask(self):
        return math.sqrt(self.content)


myObject = SomeObject(9)

print myObject.doTask()
