import pytest as pytest

from banking.domain import Customer, Account, CheckingAccount


@pytest.fixture
def a_customer_with_no_account():
    return Customer("11111111110", "jack shephard")


@pytest.fixture
def a_customer_with_four_accounts():
    jack = Customer("11111111110", "jack shephard")
    jack.add_account(Account("tr1", 10_000))
    jack.add_account(CheckingAccount("tr2", 20_000, 5_000))
    jack.add_account(Account("tr3", 30_000))
    jack.add_account(CheckingAccount("tr4", 40_000, 10_000))
    return jack


def test_creating_a_customer_with_no_account_successfully(a_customer_with_no_account):
    assert a_customer_with_no_account.identity == "11111111110"
    assert a_customer_with_no_account.full_name == "jack shephard"
    assert len(a_customer_with_no_account._accounts) == 0


def test_creating_a_customer_with_four_accounts_successfully(a_customer_with_four_accounts):
    assert a_customer_with_four_accounts.identity == "11111111110"
    assert a_customer_with_four_accounts.full_name == "jack shephard"
    assert len(a_customer_with_four_accounts._accounts) == 4
    tr1 = a_customer_with_four_accounts.get_account_by_iban("tr1")
    assert tr1 is not None
    assert tr1.iban == "tr1"
    assert tr1.balance == 10_000
    tr2 = a_customer_with_four_accounts.get_account_by_iban("tr2")
    assert tr2 is not None
    assert tr2.iban == "tr2"
    assert tr2.balance == 20_000
    assert tr2.overdraft_amount == 5_000
    tr3 = a_customer_with_four_accounts.get_account_by_iban("tr3")
    assert tr3 is not None
    assert tr3.iban == "tr3"
    assert tr3.balance == 30_000
    tr4 = a_customer_with_four_accounts.get_account_by_iban("tr4")
    assert tr4 is not None
    assert tr4.iban == "tr4"
    assert tr4.balance == 40_000
    assert tr4.overdraft_amount == 10_000
    assert a_customer_with_four_accounts.balance == 100_000
