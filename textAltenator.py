def spooky(word:str):
    newword = ""
    b = True
    for char in word:
        if b:
            newword += char.lower()
        else:
            newword += char.upper()
        b = not b
    return newword