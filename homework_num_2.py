import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000: #Робимо перевірку на мінімально та максимально допустимі значення
        return 'Неправильно введене значення min або max'
    
    tickets = random.sample(range(min, max), quantity) #Виводимо вказану кількість унікальних номерів квитків вказану кількість разів
    return tickets
        
        
print(get_numbers_ticket(1, 50, 6))
        