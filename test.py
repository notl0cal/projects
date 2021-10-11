count = 0
char = "B"
word = "BPBPPBP"
for i in word:
    if char in i:
        count += 1
print(count)
