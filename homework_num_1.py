from datetime import datetime
"""
Функція get_days_from_today розраховує кількість днів
між заданою датою і поточною датою.
"""

def get_days_from_today(date):
    date_replace = date.replace('.', '-', 2).replace('/', '-', 2).replace(':', '-', 2) #Робимо заміну символу при неправильному вводі
    conv_date = datetime.strptime(date_replace, '%Y-%m-%d').date() #Задана дата переводиться до datetime об'єкту в форматі "РРРР-ММ-ДД"
    today_date = datetime.today().date() #Поточна дата в форматі "РРРР-ММ-ДД"
    total_date = conv_date - today_date #Різниця вказаної та поточної дати    
    return total_date.days #Повернення результату різниці    

date_plus = '2026-02-01' #Задаємо дату, яка виводить результат з додатним числом
print(f'Різниця між поточною та заданою датами: {get_days_from_today(date_plus)} дня(і)')

date_minus = '2026.01.01' #Задаємо дату, яка виводить результат з від'ємним числом на неправильному написанні через "."
print(f'Різниця між поточною та заданою датами: {get_days_from_today(date_minus)} дня(і)')

date_with_slash = '2026/02/28' #Задаємо дату, яка виводить результат при неправильному написанні через "/"
print(f'Різниця між поточною та заданою датами: {get_days_from_today(date_with_slash)} дня(і)')

date_with_double_doot = '2026:03:15' #Задаємо дату, яка виводить результат при неправильному написанні через ":"
print(f'Різниця між поточною та заданою датами: {get_days_from_today(date_with_double_doot)} дня(і)')