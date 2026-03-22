def si(principal, rate, time):
    return (principal * rate * time) / 100
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))
si = si(p, r, t)
print(f"The simple interest for principal {p}, rate {r}%, and time {t} years is {si}")