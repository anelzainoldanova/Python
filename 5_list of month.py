print('list of month: January, February, March, April, May, June, July, August, September, October, November, December')
print("Input the name of Month:")
month = input()
if month=="April" or month=="June" or month=="September" or month=="November" :
    print("Num of days: 30 days")
elif month == "February":
    print("Num of days: 28/29 days")
else:
    print("Num of days: 31 days")