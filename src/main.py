from pathlib import Path

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import (
    get_transactions,
    get_transactions_csv,
    process_bank_search,
    get_transaction_excel,
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def main():
    programs = {
        "1": "Для обработки выбран JSON-файл",
        "2": "Для обработки выбран CSV-файл",
        "3": "Для обработки выбран XLSX-файл",
    }

    status_list = ["EXECUTED", "CANCELED", "PENDING"]

    yes_no_answers = {"да": True, "нет": False}
    asc_desc_answers = {"по возрастанию": False, "по убыванию": True}
    hello_string = """Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""

    ask_for_status = """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""

    ask_for_date_sort = """Отсортировать операции по дате? Да/Нет\n"""

    ask_for_asc_desc = """Отсортировать по возрастанию или по убыванию?\n"""

    ask_for_rub_transactions = """Выводить только рублевые транзакции? Да/Нет\n"""

    ask_for_description = """Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"""

    chosen_var = input(hello_string)
    if chosen_var in programs.keys():
        print(f"{programs[str(chosen_var)]}")
        if chosen_var == "1":
            transactions = get_transactions(DATA_DIR / "operations.json")
        elif chosen_var == "2":
            transactions = get_transactions_csv(DATA_DIR / "transactions.csv")
        elif chosen_var == "3":
            transactions = get_transaction_excel(DATA_DIR / "transactions_excel.xlsx")

        print(type(transactions))
        print(transactions)
        status_flag = False
        while not status_flag:
            status = input(ask_for_status)
            if status.strip().upper() in status_list:
                status_flag = True
                transactions = filter_by_state(transactions, status.strip().upper())
                print(f"Операции отфильтрованы по статусу {status.strip().upper()}")
                print(transactions)

                flag_sort_by_date_str = input(ask_for_date_sort)
                if flag_sort_by_date_str.strip().lower() == "да":
                    flag_sort_asc_desc_str = input(ask_for_asc_desc)
                    if (
                        flag_sort_asc_desc_str.strip().lower()
                        in asc_desc_answers.keys()
                    ):
                        transactions = sort_by_date(
                            transactions,
                            asc_desc_answers[flag_sort_asc_desc_str.strip().lower()],
                        )
                        print(transactions)

                flag_sort_rub_transactions_str = input(ask_for_rub_transactions)
                if (
                    flag_sort_rub_transactions_str.strip().lower()
                    in yes_no_answers.keys()
                ):
                    print(type(transactions))
                    transactions = filter_by_currency(transactions, "RUB")
                    print(transactions)
                flag_sort_description_str = input(ask_for_description)
                if flag_sort_description_str.strip().lower() == "да":
                    description_str = input(
                        "Введите ключевое слово, которое хотите найти\n"
                    )
                    transactions = process_bank_search(transactions, description_str)
                    print(transactions)

                print(type(transactions))
                print(transactions)

                if len(list(transactions)) == 0:
                    print("""Не найдено ни одной транзакции, подходящей под ваши
условия фильтрации""")
                else:
                    print(
                        f"""Распечатываю итоговый список транзакций...\n
                        Всего банковских операций в выборке: {len(list(transactions))}"""
                    )
                    for transaction in list(transactions):
                        print(transaction)

            else:
                print(f'Статус операции "{status}" недоступен')

    else:
        pass


if __name__ == "__main__":
    main()
