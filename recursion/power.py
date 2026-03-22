def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

print(f"2^3 = {power(2, 3)}")
print(f"5^0 = {power(5, 0)}")
print(f"10^2 = {power(10, 2)}")
print(f"3^4 = {power(3, 4)}")

                    