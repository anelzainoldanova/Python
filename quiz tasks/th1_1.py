import math
a = int(input())
b = int(input())
c = int(input())
d = b*b - 4*a*c
x1 = (-b - math.sqrt(d))/2*a
x2 = (-b + math.sqrt(d))/2*a
print(x1,x2)