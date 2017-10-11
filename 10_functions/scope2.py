# scope, bad practice
# don't do it!

def addition(first, second):
    # added only "lives" here
    # variable declared in 'mainline'
    added = first + second + variable
    return added

# see, defined here. Used in function
variable = 2

returned = addition(1, 2)

print returned

