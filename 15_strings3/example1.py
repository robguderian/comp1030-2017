
words = "You're a wizard 'arry."

parts = words.split()

print parts

for word in parts:
    print word
    
    cleanWord = ""
    for letter in word:
        if ((letter >= 'A' and letter <= 'Z') or 
            (letter >= 'a' and letter <= 'z')):
            cleanWord = cleanWord + letter
    print cleanWord
        
        