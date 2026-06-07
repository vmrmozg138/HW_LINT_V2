def get_mask_card_number (card_number):
    """функция для маскирования номера карты"""
    if card_number.isdigit():
        raw_str_card_number = str(card_number).replace(" ", "")
        if len(raw_str_card_number) == 16:
            formated_card_number = (
                raw_str_card_number[:6] + "*" * 6 + raw_str_card_number[-4:]
            )
            return " ".join(
                formated_card_number[i : i + 4]
                for i in range(0, len(formated_card_number), 4)
            )
        else:
            return "Ошибка! Введите корректный номер карты"
    else:
        return "Ошибка! Для ввода номера карты допускается использовать только цифры"


def get_mask_account(account):
    """функция для маскирования номера счета"""
    raw_str_account = str(account).replace(" ", "")
    if len(raw_str_account) < 6:
        return "Ошибка! Введите корректный номер счета"
    else:
        return "**" + raw_str_account[-4:]
