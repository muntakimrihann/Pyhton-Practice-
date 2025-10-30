balance = 5000

print("Welcome to World's Bank")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: {balance} TK")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited {amount} TK successfully! New balance: {balance} TK")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Withdrew {amount} TK successfully! New balance: {balance} TK")
    elif choice == "4":
        print("Thank you for using World's Bank.")
        break
    else:
        print("Invalid choice. Please enter 1–4.")
