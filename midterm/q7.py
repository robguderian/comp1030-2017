
def ifs(budget, doIt):
    cost = 100
    if cost > budget:
        print "Too bad"
    elif cost == budget:
        print "Not ideal"
    else:
        print "Good!"
    if not cost < budget and doIt:
        print "Buy"

ifs (50, True)    
