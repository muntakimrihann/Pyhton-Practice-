Name = input("Enter your Name: ")
mark = float(input("Enter your mark: "))

# Round up to 60 if mark is between 59.6 and 59.9
if 59.6 <= mark < 60:
    mark = 60

if mark >= 60:
    print("Passed")
    print("Congratulations! You've Successfully Passed the Exam")

    # Grade system
    if 60 <= mark < 70:
        grade = "D"
    elif 70 <= mark < 75:
        grade = "C"
    elif 75 <= mark < 80:
        grade = "C+"
    elif 80 <= mark < 85:
        grade = "B"
    elif 85 <= mark < 90:
        grade = "B+"
    elif 90 <= mark < 95:
        grade = "A"
    elif 95 <= mark <= 100:
        grade = "A+"
    else:
        grade = "Invalid mark range"

    print(f"Your grade is: {grade}")

else:
    grade = "F"
    print("Failed")
    print(f"Your grade is: {grade}")
    print("Alas! You Failed. Better Luck Next Time")
