import json

from src.external_api import convert_to_rub

url = "https://marketplace.apilayer.com/exchangerates_data-api"


def get_transactions(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        transactions = json.load(f)
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
        if currency == "RUB":
            return amount
        else:
            return convert_to_rub(currency, amount)
    else:
        return ""
