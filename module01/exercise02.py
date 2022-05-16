from banking import Account, InsufficientBalanceError, CheckingAccount

try:
    acc1 = CheckingAccount("tr1", 100000, 1000)
    acc1.deposit(4500)
    acc1.withdraw(105500)
    print(acc1)
    acc1.withdraw(1)
except ValueError as err:
    print(err)
except InsufficientBalanceError as err:
    print(f"An error has occurred: {err.message}")
    print(f"Deficit: {err.deficit}")
