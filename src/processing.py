def filter_by_state(dicts_list: list[dict], state="EXCLUDED"):
    """функция сортирует поданный на вход список словарей,
    осталвляет только те, у кого значение по ключу state совпадает с указанные во втором аргументе
    (по умолчанию - EXCLUDED)"""
    return list(filter(lambda d: d["state"] == state, dicts_list))


def sort_by_date(dicts_list: list[dict], reverse=True):
    """функция сортирует список словарей по дате, направление по умолчанию - по убыванию"""
    return sorted(dicts_list, key=lambda x: x["date"], reverse=reverse)
