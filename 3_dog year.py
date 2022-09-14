print("Input a dog's age in human years: ")
humanyear=int(input())
if humanyear>2:
    indogyears=10.5*2+(humanyear-2)*4
elif humanyear==2:
    indogyears=10.5*2
else:
    indogyears=10.5
print("The dog's age in dog's years is: ",indogyears)