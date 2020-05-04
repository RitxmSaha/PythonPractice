import random

list = {}

for i in range(0, 101):
    x = random.randint(1, 100)

    if x in list.keys():
        list[x] += 1
    else:
        list[x] = 1

for i in range(1, 101):
    if i not in list.keys():
        print(i, " :  0")
    else:
        print(i, " : ", list[i])

for i in sorted(list.keys()):
    print(i, " : ", list[i])
