import random

class Account:
    def __init__(self, name, initial_balance):
        self.__account_number = self._generate_account_number()
        self._name = name  # Protected
        self.__balance = initial_balance  # Private
        print(f"Account {self.__account_number} created for {self._name} with balance ${self.__balance}")

    @staticmethod
    def _generate_account_number():
        """Generates a random unique account number."""
        return random.randint(1000000000, 9999999999)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def get_balance(self):
        return self.__balance

    def _deduct_amount(self, amount):
        """Protected method for deducting balance."""
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount
        print(f"Deducted ${amount}. Remaining balance: ${self.__balance}")
