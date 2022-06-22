print("""
##############################################################
###  ✅ Vawulence Comprehensive School Course Dashboard 💥 ###
##############################################################
""")

print("""
▶ Register students
===================
""")

num_std = int(input("🚹 Enter the total number of students in the class: "))

students = [
  input("Enter the student's name: ")
  for i in range(0, num_std)
]

print()

print("""
▶ Register Subjects
===================
""")

num_sub = int(input("🔰 Enter the number of subjects for this class: "))

subjects = [input("Enter the name of the subject: ") for i in range(0, num_sub)]

print()

print("""
▶ Allocate Grades
=================
""")


def student_report(name: str, subjects_list=None) -> dict:
  if subjects_list is None:
    subjects_list = subjects
  
  print("Enter the grades for {0}".format(name))
  student_grades = [int(input("{} score: ".format(subjects[i]))) for i in range(0, len(subjects))]
  print()
  
  student_grades = dict(zip(subjects_list, student_grades))
  student_grades.update({"Name": "{}".format(name)})
  
  return student_grades


class_report = [student_report(students[i], subjects) for i in range(0, len(students))]

print("""
##############################################
###  💣 Vawulence Comprehensive School 🚀  ###
##############################################
""")


def print_scores() -> None:
  print()
