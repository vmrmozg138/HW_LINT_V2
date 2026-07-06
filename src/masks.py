import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number):
    """функция для маскирования номера карты"""
    logger.info(f"Маскируем номер карты {card_number}")
    if card_number.isdigit():
        raw_str_card_number = str(card_number).replace(" ", "")
        if len(raw_str_card_number) == 16:
            formated_card_number = (
                raw_str_card_number[:6] + "*" * 6 + raw_str_card_number[-4:]
            )
            logger.info(f"Функция выполнилась успешно")
            return " ".join(
                formated_card_number[i : i + 4]
                for i in range(0, len(formated_card_number), 4)
            )
        else:
            logger.error(f"Некорректный номер карты")
            return "Ошибка! Введите корректный номер карты"
    else:
        logger.error(f"Номер карты содержит буквы")
        return "Ошибка! Для ввода номера карты допускается использовать только цифры"


def get_mask_account(account):
    """функция для маскирования номера счета"""
    logger.info(f"Вызвана функция для маскировки номера счета {account}")
    raw_str_account = str(account).replace(" ", "")
    if account.isdigit():
        if len(raw_str_account) < 6:
            logger.error(f"Введен некорректный номер счета")
            return "Ошибка! Введите корректный номер счета"
        else:
            logger.info(f"Маскировка номера счета выполнена")
            return "**" + raw_str_account[-4:]
    else:
        logger.error(f"Номер счета содержит буквы")
        return "Ошибка! Номер счета должен состоять только из цифр"
