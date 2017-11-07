def remover(words):
    out = ""
    for letter in words:
        if not(letter >= "A" and letter <= "Z"):
            out = out + letter
    return out

print remover("Bill Gates")
print remover("Hello")