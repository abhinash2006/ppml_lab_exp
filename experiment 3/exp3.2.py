import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Not a quadratic equation")
else:
    d = b**2 - 4*a*c
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Roots: {r1}, {r2}")
    elif d == 0:
        r = -b / (2*a)
        print(f"Root: {r}")                                                          
        print("No real roots")
