chinese_zodiac_signs  = ['Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Goat']
year = int(input('Input your birth year: '))
num = year % 12
print(chinese_zodiac_signs[num])