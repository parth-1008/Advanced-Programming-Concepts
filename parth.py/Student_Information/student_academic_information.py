def academic_info():

    subject1 = float(input("Enter marks in Python: "))
    subject2 = float(input("Enter marks in Mathematics: "))
    subject3 = float(input("Enter marks in Computer Science: "))

    total = subject1 + subject2 + subject3
    average = total / 3
    percentage = (total / 300) * 100
    cgpa = percentage / 9.5

    return subject1, subject2, subject3, total, average, percentage, cgpa