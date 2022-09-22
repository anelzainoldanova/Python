n = int(input())

def factorial(a,n):
    s = 1
    for j in range(1,n+1):
        s = s*j
        j = j+1
    return s


a = []

for i in range(n):
        print(2*(i+1)*factorial(1,i+1))
        a[i+1] = 2*(i+1)*factorial(1,i+1)
        print(sum(a[i]))