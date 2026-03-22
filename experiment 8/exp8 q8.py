def large(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
largest = large(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}")