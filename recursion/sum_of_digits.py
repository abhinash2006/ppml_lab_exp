def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)
print(f"Sum of digits of 1234: {sum_of_digits(1234)}")
print(f"Sum of digits of 999: {sum_of_digits(999)}")
print(f"Sum of digits of 56: {sum_of_digits(56)}")
print(f"Sum of digits of 7: {sum_of_digits(7)}")
print(f"Sum of digits of 0: {sum_of_digits(0)}")

