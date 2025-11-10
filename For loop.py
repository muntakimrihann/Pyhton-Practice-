print(" Welcome to Text-Based Calculator")

while True:
    print("\n--- MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Module (%)")
    print("6. Power")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "7":
        print("Exiting Calculator...")
        break

    # Get numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print(" Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print(" Error: Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

    elif choice == "5":
        print("Result:", num1 % num2)

    elif choice == "6":
        print(" Result:", num1 ** num2)

    else:
        print(" Invalid choice! Try again.")
