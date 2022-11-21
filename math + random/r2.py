import random
# tickets = set(["".join(list(map(str, [random.choice(range(0, 10)) for _ in range(10)]))) for _ in range(100)])
tickets = ["".join([f"{random.choice(range(0, 10))}" for _ in range(10)]) for _ in range(100)]
print(tickets)
print(len(tickets))
[print(random.choice(tickets)) for _ in range(2)]