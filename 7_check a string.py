print("Input a string:")
string = input()
cnt = 0
for i in range(len(string)):
    if string[i].isdigit():
            cnt+=1
if cnt != 0:
    print ("The string is an integer")
else: print ("The string is not an integer")
