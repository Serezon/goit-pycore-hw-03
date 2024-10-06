import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if (min < 1 or max > 1000):
        print("Invalid range. Please use numbers between 1 and 1000.")
        return []
    if (min > max):
        print("Invalid range. Please use min smaller than max.")
        return []
    if (quantity < 1):
        print("Invalid quantity. Please use a number greater than 0.")
        return []
    if (quantity > (max - min + 1)):
        print("Invalid quantity. Please use a number smaller than the range.")
        return []

    return sorted(random.sample(range(min, max + 1), quantity))

print(get_numbers_ticket(1, 10, 3))
print(get_numbers_ticket(1, 1000, 10))
print(get_numbers_ticket(0, 1000, 10))
print(get_numbers_ticket(1, 1001, 10))
print(get_numbers_ticket(1, 1000, 0))
print(get_numbers_ticket(1, 1000, 1001))
print(get_numbers_ticket(1000, 1, 10))