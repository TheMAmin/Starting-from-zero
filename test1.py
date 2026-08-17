class bankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to the Machine")

    def deposit(self):
        amount = float(input("\nEnter the amount to deposit: "))
        self.balance += amount
        print(f"\nDeposited: ${amount:.2f}")

    def withdraw(self):
        amount = float(input("\nEnter the amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nWithdrew: ${amount:.2f}")
        else:
            print("\nInsufficient balance")

    def display(self):
        print(f"\nCurrent balance: ${self.balance:.2f}")


def main():
    account = bankAccount()

    while True:
        try:
            option = int(input(
                "\nChoose an option"
                "\n1:Deposit"
                "\n2:Withdraw"
                "\n3:Display Balance"
                "\n4:Exit Machine\n"
            ))

            if option == 1:
                account.deposit()

            elif option == 2:
                account.withdraw()

            elif option == 3:
                account.display()

            elif option == 4:
                print("Thank you for using this machine")
                break

            else:
                print("That is not a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


        
main()