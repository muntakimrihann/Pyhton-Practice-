import math

print("ADVANCED SCIENTIFIC CALCULATOR ")

while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Log (base 10)")
    print("8. Natural Log (ln)")
    print("9. Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Factorial")
    print("13. Modulus (%)")
    print("14. Exponential (e^x)")
    print("15. Log with Custom Base")
    print("16. Degrees → Radians")
    print("17. Radians → Degrees")
    print("18. Absolute Value")
    print("19. Ceiling")
    print("20. Floor")
    print("21. Exit")

    choice = input("Choose option (1–21): ")

    if choice == "21":
        print(" Exiting Scientific Calculator...")
        break

    # Single-number operations
    if choice in ["6", "7", "8", "9", "10", "11", "12", "14", "15", "16", "17", "18", "19", "20"]:
        num = float(input("Enter number: "))

        try:
            if choice == "6":
                print("Square Root =", math.sqrt(num))

            elif choice == "7":
                print("Log10 =", math.log10(num))

            elif choice == "8":
                print("Natural Log (ln) =", math.log(num))

            elif choice == "9":
                print("sin =", math.sin(math.radians(num)))

            elif choice == "10":
                print("cos =", math.cos(math.radians(num)))

            elif choice == "11":
                print("tan =", math.tan(math.radians(num)))

            elif choice == "12":
                print("Factorial =", math.factorial(int(num)))

            elif choice == "14":
                print("e^x =", math.exp(num))

            elif choice == "15":
                base = float(input("Enter log base: "))
                print("Log base", base, "=", math.log(num, base))

            elif choice == "16":
                print("Radians =", math.radians(num))

            elif choice == "17":
                print("Degrees =", math.degrees(num))

            elif choice == "18":
                print("Absolute Value =", abs(num))

            elif choice == "19":
                print("Ceiling =", math.ceil(num))

            elif choice == "20":
                print("Floor =", math.floor(num))

        except Exception as e:
            print("Error:", e)

    else:
        # Two-number operations
        if choice in ["1", "2", "3", "4", "5", "13"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result =", num1 + num2)

            elif choice == "2":
                print("Result =", num1 - num2)

            elif choice == "3":
                print("Result =", num1 * num2)

            elif choice == "4":
                if num2 == 0:
                    print(" Error: Cannot divide by zero!")
                else:
                    print("Result =", num1 / num2)

            elif choice == "5":
                print("Result =", math.pow(num1, num2))

            elif choice == "13":
                print("Modulus =", num1 % num2)

        else:
            print(" Invalid option!")
