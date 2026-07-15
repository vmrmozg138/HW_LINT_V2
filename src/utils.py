import csv
import json
import logging
from pathlib import Path
import re
from collections import Counter

import pandas as pd

from src.external_api import convert_to_rub
from src.generators import transaction_descriptions

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "logs"


url = "https://marketplace.apilayer.com/exchangerates_data-api"

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(str(DATA_DIR / "utils.log"), mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def set_file_path(file_name):
    """функция для трансформации имени файла в путь до файла"""
    return str(DATA_DIR / "data" / file_name)


def get_transactions(file_path):
    """функция для добычи транзакций из json"""
    with open(file_path, "r", encoding="utf-8") as f:
        transactions = json.load(f)
        logger.info(f"Загружено {len(transactions)} транзакций из {file_path}")
        return transactions


def get_transaction_summ_rub(transaction) -> str:
    """функция выдает сумму транзакции, в рублях, если указана сумма не в рублях, то переводит в них"""
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


def get_transactions_csv(file_path) -> list[dict]:
    """функция для считывания транзакций из csv"""
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        logger.info(f"Считаны транзакции из файла {file_path}")
        return list(reader)


def get_transaction_excel(file_path) -> list[dict]:
    """функция считывает excel, возвращает список словарей"""
    excel_data = pd.read_excel(file_path)
    logger.info(f"Считаны транзакции из файла {file_path}")
    return excel_data.to_dict("records")

def process_bank_search(data:list[dict], search:str)->list[dict]:
    """функция для поиска операций по части описания"""
    pattern = re.compile(search)
    return [item for item in data if item.get("description") is not None and pattern.search(item["description"])]

def process_bank_operations(data:list[dict], categories:list)->dict:
    """функция для подсчета и группировки операций по категориям"""
    return Counter([item for item in list(transaction_descriptions(data)) if item is not None and any(cat in item for cat in categories)])



