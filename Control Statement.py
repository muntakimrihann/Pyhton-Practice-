Name = str("Enter your Name: ")

course_name1 = input("Enter Course Name: ")
mark1 = float(input(f"Enter your mark for {course_name1}: "))

if 59.6 <= mark1 < 60:
    mark1 = 60

if mark1 >= 60:
    if 60 <= mark1 < 70:
        cgpa1 = 1.00
    elif 70 <= mark1 < 75:
        cgpa1 = 2.50
    elif 75 <= mark1 < 80:
        cgpa1 = 2.75
    elif 80 <= mark1 < 85:
        cgpa1 = 3.00
    elif 85 <= mark1 < 90:
        cgpa1 = 3.25
    elif 90 <= mark1 < 95:
        cgpa1 = 3.50
    elif 95 <= mark1 <= 100:
        cgpa1 = 4.00
    else:
        cgpa1 = 0.00
else:
    cgpa1 = 0.00

course_name2 = input("Enter Course Name: ")
mark2 = float(input(f"Enter your mark for {course_name2}: "))

if 59.6 <= mark2 < 60:
    mark2 = 60

if mark2 >= 60:
    if 60 <= mark2 < 70:
        cgpa2 = 1.00
    elif 70 <= mark2 < 75:
        cgpa2 = 2.50
    elif 75 <= mark2 < 80:
        cgpa2 = 2.75
    elif 80 <= mark2 < 85:
        cgpa2 = 3.00
    elif 85 <= mark2 < 90:
        cgpa2 = 3.25
    elif 90 <= mark2 < 95:
        cgpa2 = 3.50
    elif 95 <= mark2 <= 100:
        cgpa2 = 4.00
    else:
        cgpa2 = 0.00
else:
    cgpa2 = 0.00

course_name3 = input("Enter Course Name: ")
mark3 = float(input(f"Enter your mark for {course_name3}: "))

if 59.6 <= mark3 < 60:
    mark3 = 60

if mark3 >= 60:
    if 60 <= mark3 < 70:
        cgpa3 = 1.00
    elif 70 <= mark3 < 75:
        cgpa3 = 2.50
    elif 75 <= mark3 < 80:
        cgpa3 = 2.75
    elif 80 <= mark3 < 85:
        cgpa3 = 3.00
    elif 85 <= mark3 < 90:
        cgpa3 = 3.25
    elif 90 <= mark3 < 95:
        cgpa3 = 3.50
    elif 95 <= mark3 <= 100:
        cgpa3 = 4.00
    else:
        cgpa3 = 0.00
else:
    cgpa3 = 0.00

total_cgpa = (cgpa1 + cgpa2 + cgpa3) / 3

print("\n==============================")
print(f"Student Name: {Name}")
print(f"Average CGPA: {total_cgpa:.2f}")
print("==============================")

if total_cgpa >= 2.00:
    print("Congratulations! You Passed the Semester!")
else:
    print("You Did Not Pass. Better Luck Next Time!")
