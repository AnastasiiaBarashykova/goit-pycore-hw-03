import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []

    lottery_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 1000, 10)
print("Ваші лотерейні числа:", lottery_numbers)
