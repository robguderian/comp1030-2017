# Assignment 2 example solution


studnum = 12310
curr = studnum
summation = 0
count = 0
while curr != 0:
    summation = summation + curr % 10
    curr = curr / 10
    count = count + 1

if curr % 7 == 0 and count == 5:
    print "valid"
    # we know the student # is valid, grab grades
    grade = raw_input("Gimme a grade > ")
    numberClasses = 0
    sumOfGrades = 0
    
    while grade != "":
        if grade == "A+":
            sumOfGrades += 4.5
            numberClasses += 1
        elif grade == "A":
            sumOfGrades += 4
            numberClasses += 1
        # ...
        else:
            print "that ain't no grade"

        grade = raw_input("Gimme a grade > ")

    # out of loop, do calculation
    gpa = sumOfGrades /  numberClasses
    if gpa >= 3.0:
        print "honours"
    elif gpa <= 2.0:
        print "You need some elbow grease"
    print "gpa is %f" % gpa
    
else:
    print "invalid"
    
