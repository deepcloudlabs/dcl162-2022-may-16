from banking import Account, InsufficientBalanceError

try:
    acc1 = Account("tr1", 100000)
    acc1.deposit(4500)
    acc1.withdraw(10000)
    print(acc1.balance)
    acc1.withdraw(200000)
except ValueError as err:
    print(err)
except InsufficientBalanceError as err:
    print(f"An error has occurred: {err.message}")
    print(f"Deficit: {err.deficit}")
