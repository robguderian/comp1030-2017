# scope

def addition(first, second):
    # added only "lives" here
    added = first + second
    return added

returned = addition(1, 2)

print returned

# go boom
print added
