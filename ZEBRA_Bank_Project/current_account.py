from account import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000

    def __init__(self, name, initial_balance):
        super().__init__(name, initial_balance)

    def withdraw(self, amount):
        if self.get_balance() - amount < -CurrentAccount.OVERDRAFT_LIMIT:
            raise ValueError("Cannot exceed overdraft limit.")
        self._deduct_amount(amount)
