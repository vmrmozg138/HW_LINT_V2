def filter_by_currency(lst, currency):
    return filter(
        lambda x: (
            x["operationAmount"]["currency"]["code"] == currency
            if (
                "operationAmount" in x.keys()
                and "currency" in x["operationAmount"].keys()
                and "code" in x["operationAmount"]["currency"].keys()
            )
            else None
        ),
        lst,
    )


def transaction_descriptions(lst):
    return map(lambda x: x["description"] if "description" in x.keys() else None, lst)


def card_number_generator(start, end):
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
