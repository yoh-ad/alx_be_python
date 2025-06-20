class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with a given balance (default is 0)."""
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        """Add amount to the balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Deduct amount from the balance if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")    
