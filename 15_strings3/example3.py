

myFile = open("textfile.txt")

contents = myFile.readlines()

print contents

for line in contents:
    print line.strip()