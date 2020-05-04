import statistics
list = input("What list of number's do you want to find the centered average of?(seperate numbers by spaces, no parentheses")

list1 = (list.split(" "))

list1.sort()
print(list1)
list2 = list1[1:-1]

for i in range(0, len(list2)):
    list2[i] = int(list2[i])

list3 = statistics.mean(list2)
print(list3)

