m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("Prime numbers between", m, "and", n, "are:")

for num in range(m, n + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
