import random, string
def unique_string():
    s = "".join([random.choice(string.ascii_letters) for _ in range(random.randint(3, 10))])
    return s if len(set(s)) == len(s) else unique_string()
print(unique_string())