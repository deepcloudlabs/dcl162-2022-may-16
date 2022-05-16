import pytest as pytest

from banking.domain import InsufficientBalanceError, CheckingAccount


@pytest.fixture
def a_checking_account():
    return CheckingAccount("tr1", 10_000, 1_000)


def test_creating_a_checking_account_successfully(a_checking_account):
    assert a_checking_account.iban == "tr1"
    assert a_checking_account.balance == 10_000
    assert a_checking_account.overdraft_amount == 1_000


def test_withdraw_with_negative_amount_should_fail(a_checking_account):
    with pytest.raises(ValueError):
        a_checking_account.withdraw(-1)
    assert a_checking_account.balance == 10_000


def test_withdraw_with_zero_amount_should_fail(a_checking_account):
    with pytest.raises(ValueError):
        a_checking_account.withdraw(0)
    assert a_checking_account.balance == 10_000


def test_withdraw_above_balance_and_overdraft_amount_should_fail(a_checking_account):
    with pytest.raises(InsufficientBalanceError):
        a_checking_account.withdraw(11_001)
    assert a_checking_account.balance == 10_000


def test_withdraw_all_balance_should_success(a_checking_account):
    a_checking_account.withdraw(10_000)
    assert a_checking_account.balance == 0


def test_withdraw_under_balance_should_success(a_checking_account):
    a_checking_account.withdraw(1)
    assert a_checking_account.balance == 9999


def test_withdraw_under_balance_should_success(a_checking_account):
    a_checking_account.withdraw(11_000)
    assert a_checking_account.balance == -1_000
