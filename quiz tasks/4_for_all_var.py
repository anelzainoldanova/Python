x = 0
y = 0

for i in range(4):
    move, step = input().split()

    if move == "UP":
        y = y+int(step)
    elif move == "DOWN":
        y = y-int(step)
    elif move == "LEFT":
        x = x-int(step)
    elif move == "RIGHT":
        x = x+int(step)

print(x,y)
distance = (x**2 + y**2)**0.5
print(int(distance))
