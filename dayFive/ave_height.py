# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_height = 0
for height in student_heights:
    sum_height += height

number_student = 0
for student in number_student:
    number_student += 1
print(round(sum_height/number_student))