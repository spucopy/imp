def input_student_data():
    with open('Result.txt', 'w') as file:
        while True:
            enrollment_number = input("Enter Enrollment Number: ")
            name = input("Enter Student Name: ")
            sub1_marks = input("Enter Marks for Subject 1: ")
            sub2_marks = input("Enter Marks for Subject 2: ")
            sub3_marks = input("Enter Marks for Subject 3: ")
            sub4_marks = input("Enter Marks for Subject 4: ")
            file.write(f"{enrollment_number},{name},{sub1_marks},{sub2_marks},{sub3_marks},{sub4_marks}\n")

            more_students = input("Do you want to enter details for another student? (yes/no): ").lower()
            if more_students != 'yes':
                break

def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

def process_results():
    with open('Result.txt', 'r') as file:
        lines = file.readlines()

    grade_summary = {'A+': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    for line in lines:
        data = line.strip().split(',')
        enrollment_number, name, sub1_marks, sub2_marks, sub3_marks, sub4_marks = data
        sub1_marks, sub2_marks, sub3_marks, sub4_marks = map(int, [sub1_marks, sub2_marks, sub3_marks, sub4_marks])
        total_marks = sub1_marks + sub2_marks + sub3_marks + sub4_marks
        grade = calculate_grade(total_marks)

        print(f"Enrollment Number: {enrollment_number}")
        print(f"Name: {name}")
        print(f"Subject 1 Marks: {sub1_marks}")
        print(f"Subject 2 Marks: {sub2_marks}")
        print(f"Subject 3 Marks: {sub3_marks}")
        print(f"Subject 4 Marks: {sub4_marks}")
        print(f"Total Marks: {total_marks}")
        print(f"Grade: {grade}")
        print("=" * 100)

        result = "Pass" if grade != 'F' else "Fail"
        print(f"Enrollment Number: {enrollment_number}")
        print(f"Name: {name}")
        print(f"Marks Obtained: {total_marks}")
        print(f"Result: {result}")
        print("=" * 100)

        grade_summary[grade] += 1

    print("Grade Wise Summary:")
    for grade, count in grade_summary.items():
        print(f"Grade {grade}: {count}")
input_student_data()
process_results()