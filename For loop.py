import math

history = []  # To store calculation history

def add_history(result):
    history.append(result)


print(" ADVANCED SCIENTIFIC CALCULATOR ")

while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Log10")
    print("8. Natural Log (ln)")
    print("9. sin")
    print("10. cos")
    print("11. tan")
    print("12. Factorial")
    print("13. Modulus (%)")
    print("14. Exponential (e^x)")
    print("15. Log with Custom Base")
    print("16. Degrees → Radians")
    print("17. Radians → Degrees")
    print("18. Absolute Value")
    print("19. Ceiling")
    print("20. Floor")
    print("21. Complex Number Operations")
    print("22. Solve Linear Equation (ax + b = 0)")
    print("23. Solve Quadratic Equation")
    print("24. Matrix Addition")
    print("25. Matrix Multiplication")
    print("26. Unit Conversion")
    print("27. BMI Calculator")
    print("28. Show History")
    print("29. Exit")

    choice = input("Choose option (1–29): ")

    if choice == "29":
        print("👋 Exiting Calculator...")
        break


    if choice == "21":
        print("\n--- Complex Number Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        op = input("Choose: ")
        c1 = complex(input("Enter first complex number (a+bj): "))
        c2 = complex(input("Enter second complex number (a+bj): "))

        if op == "1":
            res = c1 + c2
        elif op == "2":
            res = c1 - c2
        elif op == "3":
            res = c1 * c2
        elif op == "4":
            res = c1 / c2
        else:
            print("Invalid")
            continue

        print("Result =", res)
        add_history(f"Complex result = {res}")
        continue


    if choice == "22":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        if a == 0:
            print("No solution (a cannot be 0).")
        else:
            x = -b / a
            print("Solution: x =", x)
            add_history(f"Linear Equation x={x}")
        continue


    if choice == "23":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        d = b**2 - 4*a*c  # discriminant

        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            print("Two real roots:", x1, "and", x2)

        elif d == 0:
            x = -b / (2*a)
            print("One real root:", x)

        else:
            real = -b / (2*a)
            imag = math.sqrt(-d) / (2*a)
            print("Complex roots:", f"{real}+{imag}j", f"{real}-{imag}j")

        continue


    if choice in ["24", "25"]:
        r = int(input("Rows: "))
        c = int(input("Columns: "))

        print("Enter Matrix A values:")
        A = [[float(input()) for _ in range(c)] for _ in range(r)]

        print("Enter Matrix B values:")
        B = [[float(input()) for _ in range(c)] for _ in range(r)]

        if choice == "24":  # addition
            result = [[A[i][j] + B[i][j] for j in range(c)] for i in range(r)]
            print("Matrix Addition Result:")
            for row in result:
                print(row)

        elif choice == "25":  # multiplication
            if len(A[0]) != len(B):
                print("Matrix multiplication not possible!")
            else:
                result = [[sum(A[i][k] * B[k][j] for k in range(len(B)))
                           for j in range(len(B[0]))] for i in range(len(A))]
                print("Matrix Multiplication Result:")
                for row in result:
                    print(row)

        continue


    if choice == "26":
        print("\n--- Unit Conversion Menu ---")
        print("1. Celsius → Fahrenheit")
        print("2. Fahrenheit → Celsius")
        print("3. Meter → Kilometer")
        print("4. Kilometer → Meter")

        u = input("Choose: ")
        val = float(input("Enter value: "))

        if u == "1":
            print("Result =", (val * 9/5) + 32)
        elif u == "2":
            print("Result =", (val - 32) * 5/9)
        elif u == "3":
            print("Result =", val / 1000)
        elif u == "4":
            print("Result =", val * 1000)
        else:
            print("Invalid option")

        continue


    if choice == "27":
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (meters): "))
        bmi = weight / (height ** 2)
        print("BMI =", bmi)
        continue


    if choice == "28":
        print("\n--- Calculation History ---")
        for item in history:
            print(item)
        continue

    if choice in ["6", "7", "8", "9", "10", "11", "12", "14", "15",
                  "16", "17", "18", "19", "20"]:
        num = float(input("Enter number: "))

        if choice == "6": print("√ =", math.sqrt(num))
        elif choice == "7": print("Log10 =", math.log10(num))
        elif choice == "8": print("ln =", math.log(num))
        elif choice == "9": print("sin =", math.sin(math.radians(num)))
        elif choice == "10": print("cos =", math.cos(math.radians(num)))
        elif choice == "11": print("tan =", math.tan(math.radians(num)))
        elif choice == "12": print("Factorial =", math.factorial(int(num)))
        elif choice == "14": print("e^x =", math.exp(num))
        elif choice == "15":
            base = float(input("Enter base: "))
            print("Log Base =", math.log(num, base))
        elif choice == "16": print("Radians =", math.radians(num))
        elif choice == "17": print("Degrees =", math.degrees(num))
        elif choice == "18": print("Absolute Value =", abs(num))
        elif choice == "19": print("Ceiling =", math.ceil(num))
        elif choice == "20": print("Floor =", math.floor(num))

        continue

    if choice in ["1", "2", "3", "4", "5", "13"]:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if choice == "1": print("Result =", n1 + n2)
        elif choice == "2": print("Result =", n1 - n2)
        elif choice == "3": print("Result =", n1 * n2)
        elif choice == "4":
            if n2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                print("Result =", n1 / n2)
        elif choice == "5": print("Result =", math.pow(n1, n2))
        elif choice == "13": print("Modulus =", n1 % n2)

    else:
        print("Invalid option!")
