import re
with open('nomerlist.txt', 'r') as the_file:
    numsfile = the_file.read().split('\n')

for num in numsfile:
    pattern = r'((?:\+\d{3})?\d{3,4}\D?\d{3}\D?\d{2}\D?\d{2})'
    x = re.findall(pattern,num)
    print(x)
