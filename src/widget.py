from masks import *
from datetime import datetime


def mask_account_card(card_or_account):
    """функция для маскировки номера карты или счета в введенной строке"""
    name, number = card_or_account.strip().rsplit(" ", maxsplit=1)

    # print(f'name: {name}, number: {number}')

    if name.lower() == "счет" and len(number) == 20:
        return card_or_account.replace(number, get_mask_account(number))
    elif name.lower() != "счет" and len(number) == 16:
        return card_or_account.replace(number, get_mask_card_number(number))
    else:
        return "Данные введены некорректно"


def get_date(date_iso):
    """функция для приведения даты из ISO к формату ДД.ММ.ГГГГ"""
    dt = datetime.fromisoformat(date_iso)
    formatted_date = dt.strftime("%d.%m.%Y")
    return formatted_date
