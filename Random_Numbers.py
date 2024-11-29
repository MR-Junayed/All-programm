import random

random_numbers = [random.randint(1000000000, 1000000000000000000000000000000000000000000 ) for _ in range(5)]
print("Random numbers:", random_numbers)

sorted_numbers = sorted(random_numbers)
print("Sorted numbers:", sorted_numbers)