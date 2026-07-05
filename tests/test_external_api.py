import os
from unittest.mock import patch

import requests
from dotenv import load_dotenv

from src.external_api import convert_to_rub


@patch("requests.get")
def test_convert_to_rub(mock_get):
    load_dotenv()
    mock_get.return_value.json.return_value = {"result": "80"}
    params = {"from": "USD", "to": "RUB", "amount": "1"}
    headers = {"apikey": os.getenv("API_KEY")}
    assert convert_to_rub("USD", "1") == "80"
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        params=params,
        headers=headers,
        timeout=5,
    )
