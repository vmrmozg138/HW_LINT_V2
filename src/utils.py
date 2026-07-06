import json
import logging

from src.external_api import convert_to_rub

url = "https://marketplace.apilayer.com/exchangerates_data-api"

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        transactions = json.load(f)
        logger.info(f"Загружено {len(transactions)} транзакций из {file_path}")
        return transactions


def get_transaction_summ_rub(transaction):
    if (
        transaction.get("operationAmount") is not None
        and transaction["operationAmount"].get("currency") is not None
        and transaction["operationAmount"]["currency"].get("code") is not None
        and transaction["operationAmount"].get("amount") is not None
    ):
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]
        logger.info(f"Запрос выполнен")
        if currency == "RUB":
            return amount
        else:
            return convert_to_rub(currency, amount)
    else:
        logger.error(f"Запрос не выполнен, не найдены данные внутри транзакции")
        return ""
