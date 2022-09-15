list1 = { 'January' : 'Capricorn',
        'February' : 'Aquarius',
        'March' : 'Pisces', 
        'April' : 'Aries', 
        'May' : 'Taurus', 
        'June' : 'Gemini', 
        'July' : 'Cancer', 
        'August' : 'Leo', 
        'September' : 'Virgo', 
        'October' : 'Libra', 
        'November' : 'Scorpio', 
        'December'  : 'Sagittarius'}

list2 = { 'January' : 'Aquarius',
        'February' : 'Pisces',
        'March' : 'Aries', 
        'April' : 'Taurus', 
        'May' : 'Gemini', 
        'June' : 'Cancer', 
        'July' : 'Leo', 
        'August' : 'Virgo', 
        'September' : 'Libra', 
        'October' : 'Scorpio', 
        'November' : 'Sagittarius', 
        'December'  : 'Capricorn'}
print ("Input birthday: ")
birthday = int(input())
print ("Input month of birth (e.g. march, july etc): ")
month = input()

if birthday<22:
        print('Your astrological sign is: ',list1[month])
else:
        print('Your astrological sign is: ',list2[month])

