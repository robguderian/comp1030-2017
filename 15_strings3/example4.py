
myFile = open("textfile.txt")

contents = myFile.read()

count = 0
for letter in contents:
    if letter == "\n":
        count += 1
        
print count


# have to reopen my file
myFile = open("textfile.txt")
contents = myFile.readlines()
print len(contents)