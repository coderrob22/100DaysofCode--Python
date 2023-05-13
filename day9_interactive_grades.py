student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for grade in student_scores:
  if student_scores[grade] > 90:
    student_grades[grade] = "Outstanding"
  elif student_scores[grade] > 80:
    student_grades[grade] = "Exceeds Expectations"
  elif student_scores[grade] > 70:
    student_grades[grade] = "Acceptable"
  else:
    student_grades[grade] = "Fail"
  

# 🚨 Don't change the code below 👇
print(student_grades)