import pytest

from src.generators import *
from tests.conftest import *


def test_filter_by_currency_USD(transactions_all, transactions_USD):
    result = list(filter_by_currency(transactions_all, "USD"))
    assert result == transactions_USD


def test_filter_by_currency_RUB(transactions_all, transactions_RUB):
    result = list(filter_by_currency(transactions_all, "RUB"))
    assert result == transactions_RUB


def test_transaction_descriptions(transactions_all, transactions_dscr_all):
    result = list(transaction_descriptions(transactions_all))
    assert result == transactions_dscr_all


def test_card_number_generator_small_limits(cards4):
    result = list(card_number_generator(start=1, end=5))
    assert result == cards4
