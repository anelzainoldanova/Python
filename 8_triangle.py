print("Input lenghts of the triangle sides:")
x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))

if x>z+y or z>x+y or y>x+z:
    print("error")#check
else:
    if x == y == z:
        print("Equilateral triangle")
    elif x == y or y == z or x == z:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")