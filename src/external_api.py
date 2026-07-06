import os

import requests
from dotenv import load_dotenv


def convert_to_rub(currency, amount):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"from": currency, "to": "RUB", "amount": amount}
    headers = {"apikey": API_KEY}
    response = requests.get(url, params=params, headers=headers, timeout=5)

    response.raise_for_status()

    return response.json()["result"]
