from datetime import datetime

def get_days_from_today(date):
    conv_date = datetime.strptime(date, '%Y.%m.%d').date() #Задана дата переводиться до datetime об'єкту в форматі "РРРР-ММ-ДД"
    today_date = datetime.today().date() #Поточна дата в форматі "РРРР-ММ-ДД"
    total_date = conv_date - today_date #Різниця вказаної та поточної дати
    
    return total_date.days #Повернення результату різниці

date_plus = '2026.02.1' #Задаємо дату, яка виводить результат з числом "+"
print(f'Різниця між поточною та заданою датами: {get_days_from_today(date_plus)} дня(і)')

date_minus = '2026.01.01' #Задаємо дату, яка виводить результат з число "-"
print(f'Різниця між поточною та заданою датами: {get_days_from_today(date_minus)} дня(і)')