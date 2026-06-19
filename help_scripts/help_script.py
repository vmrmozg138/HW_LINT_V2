from src.widget import mask_account_card, get_date

widget_raw_data = '''Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305'''

widget_test_data = ','.join(f'(\'{wrd}\', \'{mask_account_card(wrd)}\')' for wrd in widget_raw_data.split('\n'))
print(widget_test_data)

print(get_date('2024-13-11T02:26:18.671407'))