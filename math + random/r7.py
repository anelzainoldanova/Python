import random
state = random.getstate()
for i in range(6):
    if i < 5: random.setstate(state)
    print(random.randint(1, 6))