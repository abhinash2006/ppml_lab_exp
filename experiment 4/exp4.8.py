n = int(input("Enter number: "))
r = 0
while n > 0:
    r = r * 10 + n % 10
    n //= 10
print(f"Reversed: {r}")
