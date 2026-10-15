import student_information
import student_academic_information

name, roll_no, age = student_information.student_info()

subject1, subject2, subject3, total, average, percentage, cgpa = student_academic_information.academic_info()

print("\n" "STUDENT PERSONAL INFORMATION ")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Age        :", age)

print("\n""STUDENT ACADEMIC INFORMATION ")
print("Subject 1  :", subject1)
print("Subject 2  :", subject2)
print("Subject 3  :", subject3)
print("Total Marks:", total, "/ 300")
print("Average    :", round(average, 2))
print("Percentage :", round(percentage, 2), "%")
print("CGPA       :", round(cgpa, 2))