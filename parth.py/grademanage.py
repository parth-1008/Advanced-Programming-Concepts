names = []
grades = []

def add_student():
    name = input("Enter student name: ").strip()
    if name in names:
        print("That student already exists.")
        return

    grade = float(input("Enter grade: "))
    names.append(name)
    grades.append(grade)
    print("Student added successfully.")


def update_grade():
    name = input("Enter student name: ").strip()
    if name not in names:
        print("Student not found.")
        return

    grades[names.index(name)] = float(input("Enter new grade: "))
    print("Grade updated successfully.")


def remove_student():
    name = input("Enter student name: ").strip()
    if name not in names:
        print("Student not found.")
        return

    student_index = names.index(name)
    names.pop(student_index)
    grades.pop(student_index)
    print("Student removed successfully.")


def display_average():
    if not grades:
        print("No grades available.")
        return

    print(f"Class average: {sum(grades) / len(grades):.2f}")


def display_highest_lowest():
    if not grades:
        print("No grades available.")
        return

    highest_index = grades.index(max(grades))
    lowest_index = grades.index(min(grades))
    print(f"Highest grade: {names[highest_index]} ({grades[highest_index]:.2f})")
    print(f"Lowest grade: {names[lowest_index]} ({grades[lowest_index]:.2f})")


def display_menu():
    print("\n--- Student Grade Management System ---")
    print("1. Add a new student")
    print("2. Update an existing student's grade")
    print("3. Remove a student")
    print("4. Display class average grade")
    print("5. Display highest and lowest grades")
    print("6. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            display_average()
        elif choice == "5":
            display_highest_lowest()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()