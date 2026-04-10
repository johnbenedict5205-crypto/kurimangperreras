class Student_jbgp:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course
    
    def display_student_jbgp(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Course:", self.course)

student1_jbgp = Student_jbgp("Maria", "2023-001", "BSIS")
student1_jbgp.display_student_jbgp()

