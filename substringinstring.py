def subinstr(sub: str, str: str):
    counter = 0
    str = "this world is our world!"
    sub = "world"
    for i in range(len(str)):
        if sub == str[i:i+len(sub)]:
            counter += 1
    return counter

#test
print(subinstr("world", "this world is our world"))