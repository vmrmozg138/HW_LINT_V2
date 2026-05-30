from masks import *
from datetime import datetime

card_names = ['Maestro','MasterCard','Visa Classic', 'Visa Platinum', 'Visa Gold']
def mask_account_card(card_or_account):
    name, number = card_or_account.strip().rsplit(" ", maxsplit=1)

    #print(f'name: {name}, number: {number}')

    if name in card_names and len(number) == 16:
        return card_or_account.replace(number, get_mask_card_number(number))
    elif name.lower() == 'счет' and len(number) == 20:
        return card_or_account.replace(number, get_mask_account(number))
    else:
        return 'Данные введены некорректно'


def get_date(date_iso):
    dt = datetime.fromisoformat(date_iso)
    formatted_date = dt.strftime("%d.%m.%Y")
    return formatted_date
