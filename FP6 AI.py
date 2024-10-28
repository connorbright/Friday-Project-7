class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

def main():
    # Create one instance of a bank account
    account = BankAccount(account_number="12345678")

    while True:
        entered_account_number = input("Please enter your account number: ")
        
        if entered_account_number != account.account_number:
            print("Incorrect account number. Please try again.")
            continue
        
        print("What would you like to do?")
        print("a) Deposit money")
        print("b) Withdraw money")
        print("c) Check balance")
        print("d) Exit")
        
        choice = input("Enter your choice: ").lower()
        
        if choice == 'a':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 'b':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 'c':
            account.check_balance()
        elif choice == 'd':
            print("Goodbye!")
            break
        else:
            print("try again")