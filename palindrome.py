def palindrome(word:str):
    rword = ""
    for i in word:
        rword = i + rword
    if word == rword:
        return True
    return False
print(palindrome("abcdef"))