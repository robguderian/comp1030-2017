# zodiac

byear = 1997
curr = byear
while curr > 1911:
    curr -= 12

print curr
if curr == 1900:
    sign = "rat"
elif curr == 1901:
    sign = "Ox"
#.....
else:
    print "you should never see this"
    

print "you were born in %d and you are a %s" % (byear, sign)
