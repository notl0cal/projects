num = 153
result = 0
count = 0               
for i in str(num):
    result += int(i) ** len(str(num))
if result == num:
    print("True! " + str(num) + " == " + str(result))
else:
    print("False!" + str(num) + " != " + str(result))