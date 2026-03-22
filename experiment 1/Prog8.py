s1 = float(input("Enter the 1st side:"))
s2 = float(input("Enter the 2nd side:"))
s3 = float(input("Enter the 3rd side:"))
s = (s1 + s2 + s3) / 2
area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
print("Area of the triangle is:", area)