import random, string, re
def valid_string():
    password = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])
    return password if len(re.findall("\d+", password)) > 3 else valid_string()
print(valid_string())