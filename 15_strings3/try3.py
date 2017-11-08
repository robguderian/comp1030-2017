try:
    num = int(raw_input("Number > "))
    thing = 1/0
    open("not here")
except ValueError:
    print "there was a number problem!"
except IOError:
    print "file does not exist"
except:
    print "there was some other error!"
