
try:
    11/0
    myFile = open('lice.txt')
    
    for line in myFile.readlines():
        print line
# sieve
except IOError as ioe:
    print "Input Output error!"
    ioe.get
    
except ZeroDivisionError as zde:
    print "zero division!"
    
except ArithmeticError as ae:
    print "ArithmeticError"
    
except StandardError as se:
    print "standard error"
    
except ValueError:
    print "Value error"
except:
    print "I couldn't predict this!"
finally:
    print "This runs every time"
    myFile.close()
    
print "done"