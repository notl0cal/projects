num = 2000000
count = 0
while num >= 1:
    num /= 2
    if num / 2 <= 1:
        count += 1
        result = count
print(result)