def calculate_average_jbgp(grades):
    return sum(grades) / len(grades)


def get_remark_jbgp(averagegrade_jbgp):
    if averagegrade_jbgp >= 90:
        return "Excellent"
    elif averagegrade_jbgp >= 85:
        return "Very Good"
    elif averagegrade_jbgp >= 80:
        return "Good"
    elif averagegrade_jbgp >= 75:
        return "Fair"
    else:
        return "Failed"


grade1_jbgp = float(input("Enter grade for Subject 1: "))
grade2_jbgp = float(input("Enter grade for Subject 2: "))
grade3_jbgp = float(input("Enter grade for Subject 3: "))

average_grade_jbgp = calculate_average_jbgp([grade1_jbgp, grade2_jbgp, grade3_jbgp])
remark_jbgp = get_remark_jbgp(average_grade_jbgp)

print("\n----- GRADE PROCESSOR -----")
print("Average Grade:", round(average_grade_jbgp, 2))
print("Remark:", remark_jbgp)

