import random

""""
Функція get_numbers_ticket, визначає переможця(-ців) у розігращі
з унікальним номером квитка та відсортовує номери(у разі великої
кількості цих номерів)
"""""

def get_numbers_ticket(min, max, quantity): 
    empty_lst = []
    if min < 1 or max > 1000 or min > max: #Робимо перевірку на мінімально та максимально допустимі значення
        return empty_lst
    try:
        tickets = random.sample(range(min, max), quantity) #Виводимо вказану кількість унікальних номерів квитків вказану кількість разів
        tickets.sort() #Сортуємо список
        return tickets
    except:
        return empty_lst #Робимо виняток у разі некоректно введених даних
    
print(f'Переможці у розіграші: {get_numbers_ticket(1, 50, 6)}') #При введенні коректних даних       
print(f'Переможці у розіграші: {get_numbers_ticket(1000, 1200, 6)}') #При введенні некоректних даних
print(f'Переможці у розіграші: {get_numbers_ticket(1200, 1000, 6)}') #При введенні некоректних даних
print(f'Переможці у розіграші: {get_numbers_ticket(10, 14, 6)}') #При введенні некоректних даних
print(f'Переможці у розіграші: {get_numbers_ticket(14, 10, 6)}') #При введенні некоректних даних
        