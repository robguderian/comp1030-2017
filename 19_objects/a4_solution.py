
def encrypt(inStr, key):
    # 1, change to upper case
    prepPart1 = inStr.upper()
    # 2, remove anything but letters and space
    cleaned = ""
    for letter in prepPart1:
        if letter >= 'A' and letter <= 'Z' or letter == ' ':
            cleaned = cleaned + letter
    # 3, encrypt (this could be part of the loop above, if we wanted)
    encrypted = ""
    for letter in cleaned:
        # convert to ordinal, then index to 0
        if letter != " ":
            l = ord(letter) - ord('A')
            l = (l + key) % 26
            encrypted = encrypted + chr(l + ord('A'))
        else:
            # special case for space
            encrypted = encrypted + letter
    return encrypted

def decrypt(inCoded, key):
    # 1, shift
    decrypted = ""
    for letter in inCoded:
        # convert to ordinal, then index to 0
        if letter !=  " ":
            l = ord(letter) - ord('A')
            l = (l - key) % 26
            decrypted = decrypted + chr(l + ord('A'))
        else:
            # special case for " " 
            decrypted = decrypted + letter
    return decrypted


firstTest = "Hello World!"
key = 5
firstEncrypted = encrypt(firstTest, key)
print firstEncrypted
firstDecrypted = decrypt(firstEncrypted, key)
print firstDecrypted

secondTest = "Bird bird bird bird is the word"
secondEncrypted = encrypt(secondTest, key)
print secondEncrypted
secondDecrypted = decrypt(secondEncrypted, key)
print secondDecrypted