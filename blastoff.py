num_1 = 5
num_2 = 2
while num_1 > num_2:
    for i in reversed(range(num_2, num_1 + 1)):
        print(i)
    print("Blast Off!")
    break