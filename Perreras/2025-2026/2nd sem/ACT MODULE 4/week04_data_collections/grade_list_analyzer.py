grades_jbgp = []

for i_jbgp in range(5):
    grade = float(input(f"Enter grade {i_jbgp + 1}: "))
    grades_jbgp.append(grade)

average_grade_jbgp = sum(grades_jbgp) / len(grades_jbgp)
highest_grade_jbgp = max(grades_jbgp)
lowest_grade_jbgp = min(grades_jbgp)

print("\nAverage Grade:", round(average_grade_jbgp, 2))
print("Highest Grade:", highest_grade_jbgp)
print("Lowest Grade:", lowest_grade_jbgp)

