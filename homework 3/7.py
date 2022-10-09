import re 
date = input("Enter date: ") 
month = {
    "Jan": 1, 
    "Feb": 2, 
    "Mar": 3, 
    "Apr": 4, 
    "May": 5, 
    "Jun": 6, 
    "Jul": 7, 
    "Aug": 8, 
    "Sep": 9, 
    "Oct": 10, 
    "Nov": 11, 
    "Dec": 12
    } 
pattern = "^([^\d]{3}).+[\W]+(\d+)[\W]+(\d+)$" 
if re.search(pattern, date):  
    mon, day, year = re.findall(pattern, date)[0] 
    mon = mon.capitalize() 
    d, year = map(int, [day, year]) 
    if mon in month: print(f"{month[mon]}/{day}/{year}") 
else: print("Invalid date")