def palindrome(word:str):
    word = word.replace(" ", "")
    if word == word[::-1]:
        return True
    return False
print(palindrome("tacocat"))