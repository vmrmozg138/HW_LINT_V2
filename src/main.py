from masks import get_mask_account, get_mask_card_number
from widget import mask_account_card

card_number = input("Введите номер карты")
result = get_mask_card_number(card_number)

print(result)

account = input("Введите номер счета")
result_account = get_mask_account(account)

print(result_account)
