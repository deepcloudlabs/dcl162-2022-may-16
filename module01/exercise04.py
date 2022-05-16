from banking import Account, CheckingAccount

# generic --> polymorphism, open-close principles
def hesap_isletim_ucreti_kes(accts, amount):
    for acc in accts:
        acc.withdraw(amount)


def print_accounts(accts):
    for acc in accts:
        print(acc)


accounts = [
    Account("tr1", 10000),
    CheckingAccount("tr2", 20000),
    Account("tr3", 30000),
    CheckingAccount("tr4", 40000)
]

print_accounts(accounts)
hesap_isletim_ucreti_kes(accounts, 10)
print_accounts(accounts)
