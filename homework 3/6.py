def isValid(card): 
    import re 
    invalid_nums = [f"{i}" * 4 for i in range(10)] 
    for i in invalid_nums: 
        if re.search(i, re.sub("-", "", card)): return False 
    if re.search("[^\d-]", card): return False 
    if re.search("^[^456]", card): return False 
    if re.search("\d{4}[-]?\d{4}[-]?\d{4}[-]?\d{4}", card): return True 
    return False 

numcards = open("numcards.txt", "r").read().split("\n") 
for line in numcards: 
    if isValid(line): print(f"{line:<30}Valid") 
    else: print(f"{line:<30}Invalid")