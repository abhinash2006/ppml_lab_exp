def count_digits(n):
    n = abs(n) 
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
print(f"Digits in 12345: {count_digits(12345)}")
print(f"Digits in 999: {count_digits(999)}")
print(f"Digits in 5: {count_digits(5)}")
print(f"Digits in 0: {count_digits(0)}")
print(f"Digits in 1000000: {count_digits(1000000)}")
