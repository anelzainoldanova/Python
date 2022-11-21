import random, string
print("".join(random.choices(string.punctuation, k = random.randint(3, 10))))