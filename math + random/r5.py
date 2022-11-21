import random
from itertools import permutations
def check(password):
    l = [chr(ch) for ch in range(ord("a"), ord("z") +  1)]
    u = [chr(ch) for ch in range(ord("A"), ord("Z") + 1)]
    n = [str(i) for i in range(10)]
    s = list("/?!=+()#@%$*-,.:;><[]\\{|}'\"~")
    up = lw = d = sb = 0
    for i in password:
        if i in u: up += 1
        if i in l: lw += 1
        if i in n: d += 1
        if i in s: sb += 1
    return True if up > 1 and lw > 0 and d > 0 and sb > 0 else False

def random_password():
    password = "".join([random.choice([chr(i) for i in range(33, 127)]) for _ in range(10)]) # by ascii table
    return password if check(password) else random_password()

print(random_password())