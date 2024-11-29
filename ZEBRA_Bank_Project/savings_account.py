from account import Account

class SavingsAccount(Account):
    MINIMUM_BALANCE = 500

    def __init__(self, name, initial_balance):
        if initial_balance < SavingsAccount.MINIMUM_BALANCE:
            raise ValueError(f"Initial balance must be at least ${SavingsAccount.MINIMUM_BALANCE}.")
        super().__init__(name, initial_balance)

    def withdraw(self, amount):
        if self.get_balance() - amount < SavingsAccount.MINIMUM_BALANCE:
            raise ValueError("Cannot withdraw below the minimum balance.")
        self._deduct_amount(amount)
