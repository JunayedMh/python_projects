class ATM:
    def __init__(self,balance: float = 1000):
        self.balance = balance

    def get_amount(self,label:str):
        try:
            return float(input(f"Enter amount: {label}: $"))
        except ValueError:
            print("Invalid amount")
            return None
    
    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self,amt: float):
        if amt <= 0:
            print(" Deposit amount must be greater than 0.")
        else:
            self.balance += amt
            print(f"${amt} deposit was successfull, Your new balance is ${self.balance}.")
    
    def withdraw(self,amt:float):
        if amt <=0:
            print("Withdraw amount should be greater than 0.")
        elif amt > self.balance:
            print("You have insufficient balance")
        else:
            self.balance -= amt
            print(f"${amt} withdraw was successful, your current balance is ${self.balance}.")

    def run(self):
        print("Welcome to the 24/7 ATM bank.")
        while True:
            print("\n1.Check Balance 2.Deposit 3.Withdraw 4.Exit")
            choice = input("Option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                amt = self.get_amount("Deposit amount")
                if amt:
                    self.deposit(amt)
            elif choice == "3":
                amt = self.get_amount("Withdraw amount")
                if amt:
                    self.withdraw(amt)
            elif choice == "4":
                print("Thanks for using 24/7 ATM.")
                break
            else:
                print("Invalid Option.")
            again = input("Back to the option? Y/N: ")
            again = again.strip().lower()

            if again == "n":
                print("Thanks for using ATM")
                break

ATM().run()