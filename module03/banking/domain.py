from functools import reduce


class InsufficientBalanceError(Exception):  # inheritance
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit


class Account:
    def __init__(self, iban, balance=0):
        self._iban = iban
        self._balance = balance

    @property
    def iban(self):
        return self._iban

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        print("Account::withdraw")
        # validation
        if amount <= 0:
            raise ValueError("withdraw amount must be positive.")
        # business rule
        if amount > self._balance:
            deficit = amount - self._balance
            raise InsufficientBalanceError("your balance does not cover your expenses", deficit)
        self._balance = self._balance - amount

    def deposit(self, amount):
        # validation
        if amount <= 0:
            raise ValueError("deposit amount must be positive.")
        self._balance = self._balance + amount

    def __str__(self):
        return f"Account [iban: {self._iban}, balance: {self._balance}]"


class CheckingAccount(Account):
    """
    CheckingAccount : Derived Class, Sub-class
    Account         : Base Class, Super-class
    """

    def __init__(self, iban, balance, overdraft_amount=500):
        super().__init__(iban, balance)
        self._overdraft_amount = overdraft_amount

    @property
    def overdraft_amount(self):
        return self._overdraft_amount

    # overriding
    def withdraw(self, amount):
        print("CheckingAccount::withdraw")
        # validation
        if amount <= 0:
            raise ValueError("withdraw amount must be positive.")
        # business rule
        if amount > (self._balance + self._overdraft_amount):
            deficit = amount - self._balance - self._overdraft_amount
            raise InsufficientBalanceError("your balance does not cover your expenses", deficit)
        self._balance = self._balance - amount

    # overriding
    def __str__(self):
        return f"CheckingAccount [iban: {self._iban}, balance: {self._balance}, overdraft_amount: {self._overdraft_amount}]"


class Customer:
    def __init__(self, identity, full_name, accounts=[]):
        self._identity = identity
        self._full_name = full_name
        self._accounts = accounts

    @property
    def identity(self):
        return self._identity

    @property
    def full_name(self):
        return self._full_name

    @property
    def balance(self):
        total_balance = 0
        for acc in self._accounts:
            total_balance = total_balance + acc.balance
        return total_balance

    @property
    def balance_fun(self):
        return reduce(lambda x, y: x + y, map(lambda acc: acc.balance, self._accounts), 0)

    def add_account(self, acc):
        self._accounts.append(acc)

    def get_account_by_iban(self, iban):
        for acc in self._accounts:
            if acc.iban == iban:
                return acc
        return None
