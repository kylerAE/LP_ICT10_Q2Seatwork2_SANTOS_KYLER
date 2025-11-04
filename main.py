


subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]
units = (1, 1, 1, 1, 1, 1)


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

grades = []
for subject in subjects:
    grade = float(input(f"Enter grade for {subject}: "))
    grades.append(grade)


total = sum([grades[i] * units[i] for i in range(len(subjects))])
gwa = total / sum(units)

print("\n===== Student Grade Summary =====")
print(f"Name: {first_name} {last_name}")
for i, subject in enumerate(subjects):
    print(f"{subject}: {grades[i]}")
print(f"\nYour general weighted average is {gwa:.2f}")
