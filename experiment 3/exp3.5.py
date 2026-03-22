marks = []
for i in range(5):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = (total / 250) * 100

if percentage >= 90:
    grade = 'O'
elif percentage >= 80:
    grade = 'E'
elif percentage >= 70:
    grade = 'A'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
else:
    grade = 'F'

print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
