Name = input("Enter your Name: ")
course_name1 = input("Enter Course 1 Name: ")
mark1 = float(input(f"Enter your mark for {course_name1}: "))
credit1 = float(input(f"Enter Credit Hours for {course_name1}: "))

if 59.6 <= mark1 < 60:
    mark1 = 60

if mark1 >= 60:
    if 60 <= mark1 < 70:
        grade1 = "D"
        cgpa1 = 1.00
    elif 70 <= mark1 < 75:
        grade1 = "C"
        cgpa1 = 2.50
    elif 75 <= mark1 < 80:
        grade1 = "C+"
        cgpa1 = 2.75
    elif 80 <= mark1 < 85:
        grade1 = "B"
        cgpa1 = 3.00
    elif 85 <= mark1 < 90:
        grade1 = "B+"
        cgpa1 = 3.25
    elif 90 <= mark1 < 95:
        grade1 = "A"
        cgpa1 = 3.50
    elif 95 <= mark1 <= 100:
        grade1 = "A+"
        cgpa1 = 4.00
    else:
        grade1 = "Invalid"
        cgpa1 = 0.00
else:
    grade1 = "F"
    cgpa1 = 0.00

print(f"Your Grade in {course_name1}: {grade1}")
print(f"CGPA in {course_name1}: {cgpa1}")
print(f"Credit Hours: {credit1}")

course_name2 = input("\nEnter Course 2 Name: ")
mark2 = float(input(f"Enter your mark for {course_name2}: "))
credit2 = float(input(f"Enter Credit Hours for {course_name2}: "))

if 59.6 <= mark2 < 60:
    mark2 = 60

if mark2 >= 60:
    if 60 <= mark2 < 70:
        grade2 = "D"
        cgpa2 = 1.00
    elif 70 <= mark2 < 75:
        grade2 = "C"
        cgpa2 = 2.50
    elif 75 <= mark2 < 80:
        grade2 = "C+"
        cgpa2 = 2.75
    elif 80 <= mark2 < 85:
        grade2 = "B"
        cgpa2 = 3.00
    elif 85 <= mark2 < 90:
        grade2 = "B+"
        cgpa2 = 3.25
    elif 90 <= mark2 < 95:
        grade2 = "A"
        cgpa2 = 3.50
    elif 95 <= mark2 <= 100:
        grade2 = "A+"
        cgpa2 = 4.00
    else:
        grade2 = "Invalid"
        cgpa2 = 0.00
else:
    grade2 = "F"
    cgpa2 = 0.00

print(f"Your Grade in {course_name2}: {grade2}")
print(f"CGPA in {course_name2}: {cgpa2}")
print(f"Credit Hours: {credit2}")

course_name3 = input("\nEnter Course 3 Name: ")
mark3 = float(input(f"Enter your mark for {course_name3}: "))
credit3 = float(input(f"Enter Credit Hours for {course_name3}: "))

if 59.6 <= mark3 < 60:
    mark3 = 60

if mark3 >= 60:
    if 60 <= mark3 < 70:
        grade3 = "D"
        cgpa3 = 1.00
    elif 70 <= mark3 < 75:
        grade3 = "C"
        cgpa3 = 2.50
    elif 75 <= mark3 < 80:
        grade3 = "C+"
        cgpa3 = 2.75
    elif 80 <= mark3 < 85:
        grade3 = "B"
        cgpa3 = 3.00
    elif 85 <= mark3 < 90:
        grade3 = "B+"
        cgpa3 = 3.25
    elif 90 <= mark3 < 95:
        grade3 = "A"
        cgpa3 = 3.50
    elif 95 <= mark3 <= 100:
        grade3 = "A+"
        cgpa3 = 4.00
    else:
        grade3 = "Invalid"
        cgpa3 = 0.00
else:
    grade3 = "F"
    cgpa3 = 0.00

print(f"Your Grade in {course_name3}: {grade3}")
print(f"CGPA in {course_name3}: {cgpa3}")
print(f"Credit Hours: {credit3}")

total_credits = credit1 + credit2 + credit3
weighted_cgpa = ((cgpa1 * credit1) + (cgpa2 * credit2) + (cgpa3 * credit3)) / total_credits

print(f"Student Name: {Name}")
print(f"Total Credit Hours: {total_credits}")
print(f"Weighted Average CGPA: {weighted_cgpa:.2f}")

if weighted_cgpa >= 2.00:
    print("Congratulations! You Passed the Semester!")
else:
    print("You Did Not Pass. You're on Academic Probation!")
