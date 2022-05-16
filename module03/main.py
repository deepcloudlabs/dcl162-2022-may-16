from banking.domain import Customer, Account, CheckingAccount

if __name__ == '__main__':
    jack = Customer("11111111110", "jack bauer")
    jack.add_account(Account("tr1", 10000))
    jack.add_account(CheckingAccount("tr2", 20000, 1500))
    print(jack.balance_fun)