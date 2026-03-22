#display  simple interest  and  compound interest 
p = 1000  
r = 5     
t = 2     
si = (p * r * t) / 100
print("Simple Interest =", si)

ci = p * ((1 + r/100)**t) - p
print("Compound Interest =", ci)