import pytest as pytest

from banking.domain import Account, InsufficientBalanceError


@pytest.fixture
def an_account():
    return Account("tr1", 10_000)


def test_creating_an_account_successfully(an_account):
    assert an_account.iban == "tr1"
    assert an_account.balance == 10_000


@pytest.mark.parametrize("amount", [(-1), (-0.1), (0.0)])
def test_withdraw_with_negative_amount_should_fail(an_account, amount):
    with pytest.raises(ValueError):
        an_account.withdraw(amount)
    assert an_account.balance == 10_000


@pytest.mark.parametrize("amount", [(10001), (10001.01), (10001.1)])
def test_withdraw_above_balance_should_fail(an_account, amount):
    with pytest.raises(InsufficientBalanceError):
        an_account.withdraw(amount)
    assert an_account.balance == 10_000


def test_withdraw_all_balance_should_success(an_account):
    an_account.withdraw(10_000)
    assert an_account.balance == 0


def test_withdraw_under_balance_should_success(an_account):
    an_account.withdraw(1)
    assert an_account.balance == 9999


def test_deposit_with_negative_amount_should_fail(an_account):
    with pytest.raises(ValueError):
        an_account.deposit(-1)
    assert an_account.balance == 10_000


def test_deposit_with_zero_amount_should_fail(an_account):
    with pytest.raises(ValueError):
        an_account.deposit(0)
    assert an_account.balance == 10_000


def test_deposit_with_positive_amount_should_succeed(an_account):
    an_account.deposit(1)
    assert an_account.balance == 10_001
