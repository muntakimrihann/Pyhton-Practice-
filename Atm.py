balance = 5000
print("🏦 Welcome to Python Bank 🏦")
while True:
    print("\n Main Menu ")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Send Money")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ")

    if choice == "1":
        print(f"Your current balance is: {balance} TK")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited {amount} TK successfully!")
        print(f"New balance: {balance} TK")

    elif choice == "3":
        print("\nWithdraw Options:")
        print("1. Bank Withdrawal")
        print("2. Agent Withdrawal")
        sub_choice = input("Choose withdrawal method (1 or 2): ")

        amount = float(input("Enter amount to withdraw: "))

        if amount > balance:
            print(" Insufficient balance!")
        else:
            if sub_choice == "1":
                print(" Bank Withdrawal selected.")
                balance -= amount
                print(f" Withdrawn {amount} TK from bank.")
            elif sub_choice == "2":
                print(" Agent Withdrawal selected.")
                agent_fee = 10  # small fee for agent
                total = amount + agent_fee
                if total > balance:
                    print(" Not enough balance to cover agent fee!")
                else:
                    balance -= total
                    print(f" Withdrawn {amount} TK via agent (Fee: {agent_fee} TK).")
            else:
                print("️ Invalid withdrawal option.")

            print(f"Remaining balance: {balance} TK")

    elif choice == "4":
        receiver = input("Enter receiver account number: ")
        amount = float(input("Enter amount to send: "))

        if amount > balance:
            print(" Insufficient balance for transfer!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            balance -= amount
            print(f" Successfully sent {amount} TK to account {receiver}.")
            print(f"Remaining balance: {balance} TK")

    elif choice == "5":
        print(" Thank you for using Python Bank. Goodbye!")

    else:
        print("️ Invalid choice. Please enter a number from 1–5.")
