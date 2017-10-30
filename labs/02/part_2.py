
weightString = raw_input("What is your weight in kgs? > ")
heightString = raw_input("What is your height in m? > ")

weight = float(weightString)
height = float(heightString)

calc = weight / height

print "Your BMI is " + str(calc)
