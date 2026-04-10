student_name_jbgp = input("Enter student name: ")

grade1_jbgp = float(input("Enter grade for Subject 1: "))
grade2_jbgp = float(input("Enter grade for Subject 2: "))
grade3_jbgp = float(input("Enter grade for Subject 3: "))

average_grade_jbgp = (grade1_jbgp + grade2_jbgp + grade3_jbgp) / 3

if average_grade_jbgp >= 90:
    remark_jbgp = "Excellent"
elif average_grade_jbgp >= 85:
    remark_jbgp = "Very Good"
elif average_grade_jbgp >= 80:
    remark_jbgp = "Good"
elif average_grade_jbgp >= 75:
    remark_jbgp = "Fair"
else:
    remark_jbgp = "Failed"

print("\n----- STUDENT GRADE ANALYZER -----")
print("Student Name:", student_name_jbgp)
print("Average Grade:", round(average_grade_jbgp, 2))
print("Remark:", remark_jbgp)

