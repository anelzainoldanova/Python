str = input()
def findall(s,l):
    for i in range(len(s)):
        if 'a' == s[i]:
            print(i+1)
findall(str,'a')