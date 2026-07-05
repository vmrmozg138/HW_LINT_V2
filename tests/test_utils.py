import pytest

from src.utils import get_transaction_summ_rub


@pytest.mark.parametrize(
    "transaction, result",
    [
        (
            {
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            "",
        ),
        (
            {
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            "",
        ),
        (
            {
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            "",
        ),
    ],
)
def test_get_transaction_summ_rub_bad_input(transaction, result):
    assert get_transaction_summ_rub(transaction) == result
