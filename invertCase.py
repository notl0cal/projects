word = ""
result = ""
for char in word:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()