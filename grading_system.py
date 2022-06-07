user_grade = int(input("Enter the student's grade: "))

if user_grade >= 70:
  print("The student's grade is A! Congratulations!")
elif 65 <= user_grade < 70:
  print("The student's grade is B")
elif 60 <= user_grade < 65:
  print("Average student. Scored a C.")
else:
  print("I never even care grade again! Na fail!")
