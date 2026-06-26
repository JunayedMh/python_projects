balance = 1000
print("Welcome to 24/7 ATM Booth..")

while True:
    print("Please select the number of the option you want to use.")
    print()
    print("\n 1. Check balance 2. Deposit 3. Withdraw 4. Exit")
    print()
    choice = (input("Please choose the option above: "))

    if choice == "1":
        print(f"You have a current balance of ${balance}")

    elif choice == "2":
        try:
            amt = float(input("How much you want to deposit?: "))
            if amt <0:
                print("Amount must be greater than 0.")
            else:
                balance += amt
                print(f"${amt} has been deposited. Your current balanec is ${balance}.")
        except ValueError:
            print("Invalid Amount.")

    elif choice == "3":
        try:
            print(f"Your current balance is ${balance}.")
            withd_amt = float(input("How much you want to withdraw?: "))
            if withd_amt < 0:
                print('Amount must be greater than 0.')
            elif withd_amt > balance:
                print('You do not have sufficient balance!')
            else:
                balance -= withd_amt
                print(f"${withd_amt} was successfull, your current balance is ${balance}.")
        except ValueError:
            print("Enter a valid number.")
    elif choice == "4":
        print(f"Thanks for your ATM, your account has ${balance}.")
        break
    else:
        print("Invalid Option.")
    
    again = input("back to the option? y/n: ")
    again = again.strip().lower()

    if again == "n":
        print("Thanks for using ATM")
        break
    