import math

print("SCIENTIFIC CALCULATOR")

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
    print("12. Exit")

    choice = input("Choose option (1–12): ")

    if choice == "12":
        print("👋 Exiting Scientific Calculator...")
        break

    if choice in ["6", "7", "8", "9", "10", "11"]:
        num = float(input("Enter number: "))

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

    else:

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

        else:
            print("Invalid option!")
