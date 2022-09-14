list = { '01' :'January',
        '02' : 'February',
        '03' : 'March', 
        '04' : 'April', 
        '05' : 'May', 
        '06' : 'June', 
        '07' : 'July', 
        '08' : 'August', 
        '09' : 'September', 
        '10' : 'October', 
        '11' : 'November', 
        '12' : 'December' }

print('input the month (e.g. [1-12]):')
num = input()
print('Input the day:')
day = input()
season = ""

if num=='01' or num=='02' or num=='12':
    season = 'winter'
elif num=='03' or num=='04' or num=='05':
    season = 'spring'
elif num=='06' or num=='07' or num=='08':
    season = 'summer'
elif num=='09' or num=='10' or num=='11':
    season = "autumn"
else:
    season = "g"

if num in list:
    print(list[num]+","+day+". Season is "+season) 

