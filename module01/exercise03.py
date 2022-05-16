from random import random

from banking import Account, CheckingAccount

acc1 = None
if random() < 0.5:
    print("head")
    acc1 = Account("tr1", 10000)
else:
    print("tail")
    acc1 = CheckingAccount("tr2", 20000, 1000)
acc1.withdraw(500)
