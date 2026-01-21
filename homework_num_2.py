import random

""""
Функція get_numbers_ticket, визначає переможця(-ців) у розігращі
з унікальним номером квитка та відсортовує номери(у разі великої
кількості цих номерів)
"""""

def get_numbers_ticket(min, max, quantity): 
    empty_lst = []
    if min < 1 or max > 1000: #Робимо перевірку на мінімально та максимально допустимі значення
        return empty_lst 
    
    tickets = random.sample(range(min, max), quantity) #Виводимо вказану кількість унікальних номерів квитків вказану кількість разів
    tickets.sort() #Сортуємо список
    return tickets
        
print(f'Переможці у розіграші: {get_numbers_ticket(1, 50, 6)}') #При введенні коректних даних       
print(f'Переможці у розіграші: {get_numbers_ticket(1000, 1200, 6)}') #При введенні некоректних даних
        