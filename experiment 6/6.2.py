d1 = {}

for i in range(3):
    k = (input('Enter key : '))
    v = (input('Enter value : '))
    d1[k] = v

d2 = {}
for i, j in d1.items():
    d2[j] = i

print('D1')
for i, j in d1.items():
    print(i, j)

print('D2')
for i, j in d2.items():
    print(i, j)