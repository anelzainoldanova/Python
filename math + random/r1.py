import random
print(random.choices([n for n in range(100, 1000) if n % 5 == 0], k = 3))