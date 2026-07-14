def filter_by_state(
    dicts_list: list[dict[str, str | int]], state="EXECUTED"
) -> list[dict[str, str | int]]:
    """Функция сортирует поданный на вход список словарей,
    оставляет только те, у кого значение по ключу state совпадает с указанным во втором аргументе
    (по умолчанию - EXECUTED)"""
    return list(filter(lambda d: d.get("state") == state, dicts_list))


def sort_by_date(
    dicts_list: list[dict[str, str | int]], reverse=True
) -> list[dict[str, str | int]]:
    """Функция сортирует список словарей по дате, направление по умолчанию - по убыванию"""
    return sorted(dicts_list, key=lambda x: x["date"], reverse=reverse)
