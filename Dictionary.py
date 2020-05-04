x = {1: '1',
     2: '2'}
z = 0
print(x[1])
x[3] = '3'
print(x)

for i in range(1,(len(x)+1)):
    z = z + int(x[i])

print(z)