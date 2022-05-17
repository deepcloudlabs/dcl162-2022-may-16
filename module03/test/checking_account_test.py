import pytest as pytest

from banking.domain import InsufficientBalanceError, CheckingAccount


@pytest.fixture
def a_checking_account():
    return CheckingAccount("tr1", 10_000, 1_000)


def test_creating_a_checking_account_successfully(a_checking_account):
    assert a_checking_account.iban == "tr1"
    assert a_checking_account.balance == 10_000
    assert a_checking_account.overdraft_amount == 1_000


@pytest.mark.parametrize("amount", [(-1), (-0.1), (0.0)])
def test_withdraw_with_negative_amount_should_fail(a_checking_account, amount):
    with pytest.raises(ValueError):
        a_checking_account.withdraw(amount)
    assert a_checking_account.balance == 10_000


@pytest.mark.parametrize("amount", [(11_001), (11_001.01), (11_001.001)])
def test_withdraw_above_balance_and_overdraft_amount_should_fail(a_checking_account, amount):
    with pytest.raises(InsufficientBalanceError):
        a_checking_account.withdraw(amount)
    assert a_checking_account.balance == 10_000


@pytest.mark.parametrize("amount,expected", [(1, 9999), (2, 9998), (10_001, -1), (11_000, -1_000)])
def test_withdraw_under_balance_should_success(a_checking_account, amount, expected):
    print(amount,expected)
    a_checking_account.withdraw(amount)
    assert a_checking_account.balance == expected


def test_withdraw_all_balance_should_success(a_checking_account):
    a_checking_account.withdraw(10_000)
    assert a_checking_account.balance == 0


def test_withdraw_under_balance_should_success(a_checking_account):
    a_checking_account.withdraw(11_000)
    assert a_checking_account.balance == -1_000
