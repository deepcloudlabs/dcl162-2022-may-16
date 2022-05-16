from banking import Customer, Account, CheckingAccount

jack = Customer("11111111110", "jack shephard")
jack.add_account(Account("tr1", 10000))
jack.add_account(CheckingAccount("tr2", 20000))
jack.add_account(Account("tr3", 30000))
jack.add_account(CheckingAccount("tr4", 40000))

print(jack.balance)

acc3 = jack.get_account_by_iban("tr3")
if acc3 is not None:
    acc3.withdraw(acc3.balance)

print(jack.balance)
