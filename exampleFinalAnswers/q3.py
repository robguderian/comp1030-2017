class Stats:
    def __init__(self):
        self.data = []
    
    def addValue(self, value):
        self.data.append(value)
    
    def __str__(self):
        output = "No data!"
        if len(self.data) > 0:
            avg = sum(self.data) / len(self.data)
            output = "Values: " 
            for value in self.data:
                output = output + " " + str(value)
            output = output + "\n"
            output = output + "Average: " + str(avg) + "\n"
            output = output + "Max: " + str(max(self.data)) + "\n"
            output = output + "Min: " + str(min(self.data)) + "\n"
        return output

# tests, you do not need to write these on your final
statsObj = Stats()
print(statsObj)

statsObj.addValue(10)
statsObj.addValue(20)
statsObj.addValue(50)
statsObj.addValue(100)
print(statsObj)