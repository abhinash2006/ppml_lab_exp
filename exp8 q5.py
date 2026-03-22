def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
num = int(input("Enter the number:"))
result = prime(num)
if result:
    print(f"The number {num} is Prime")
else:
    print(f"The number {num} is Not Prime")