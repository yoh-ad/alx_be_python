class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


    
