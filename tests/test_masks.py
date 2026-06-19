import pytest
from src.masks import get_mask_card_number, get_mask_account
from tests.conftest import correct_card_number, too_long_card_number, not_numeric_card_number


@pytest.mark.parametrize(
    "open_number, masked_number",
    [('7000792289606361', '7000 79** **** 6361'),
     ('70007922896063612', 'Ошибка! Введите корректный номер карты'),
     ('7000792289asdf606361', 'Ошибка! Для ввода номера карты допускается использовать только цифры'),
     ('', 'Ошибка! Для ввода номера карты допускается использовать только цифры')])
def test_get_mask_card_number(open_number, masked_number):
    assert get_mask_card_number(open_number) == masked_number


@pytest.mark.parametrize(
    "open_account, masked_account",
    [('73654108430135874305','**4305'),
     ('12345','Ошибка! Введите корректный номер счета'),
     ('sfgsdfg', 'Ошибка! Номер счета должен состоять только из цифр')
     ])
def test_get_mask_account(open_account, masked_account):
    assert get_mask_account(open_account) == masked_account