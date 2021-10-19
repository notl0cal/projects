def mvmnt(string:str):
    n = 0
    s = 0
    w = 0
    e = 0
    for letter in string:
        if letter == "N":
            n += 1
        elif letter == "S":
            s += 1
        elif letter == "W":
            w += 1
        elif letter == "E":
            e += 1
    if n > s:
        y = "N"
    elif s > n:
        y = "S"
    else:
        y = ""
    if w > e:
        x = "W"
    elif e > w:
        x = "E"
    else:
        x = ""
    result = y + x
    return result


print(mvmnt("NNNNNSSssSSSSSSSSSWWWWWWWWWWWWWWWWWWWWEEeeeeeeeEEEE"))