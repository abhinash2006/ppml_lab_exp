s = input('Enter a sentence : ')

lst1 = s.split()

for i, j in enumerate(lst1):
    print(i, j)

lst2 = list(map(int, input(f'Enter {len(lst1)} numbers : ').split()))
lst3 = zip(lst1, lst2)

print(*lst3)