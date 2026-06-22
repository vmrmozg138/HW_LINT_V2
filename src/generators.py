def filter_by_currency(lst, currency):
    """Функция для фильтрации списка входных операций по заданной валюте(если в данных нет указанной в агрументе валюты, то вернет None)"""
    return filter(
        lambda x: (
            x["operationAmount"]["currency"]["code"] == currency
            if (
                x.get("operationAmount") is not None
                and x["operationAmount"].get("currency") is not None
                and x["operationAmount"]["currency"].get("code") is not None
            )
            else None
        ),
        lst,
    )


def transaction_descriptions(lst):
    """Функция для выделения только описания транзакций из полного списка транзакций"""
    return map(lambda x: x["description"] if "description" in x.keys() else None, lst)


def card_number_generator(start, end):
    """Функция для генерации номеров карт"""
    if end > start:
        tmpl = "xxxxxxxxxxxxxxxx"
        res = (
            " ".join(
                [
                    (tmpl[: -len(str(i))] + str(i))[j : j + 4]
                    for j in range(0, len(tmpl), 4)
                ]
            )
            for i in range(start, end)
        )
        return res
    else:
        return "Неверно указаны границы диапазона"
