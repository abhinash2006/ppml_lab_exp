a = 0
b = 1
sum_fib = 0

print("Fibonacci series up to 1000:")

while a <= 1000:
    print(a, end=" ")
    sum_fib = sum_fib + a
    c = a + b
    a = b
    b = c

print("\nSum of Fibonacci numbers:", sum_fib)
              