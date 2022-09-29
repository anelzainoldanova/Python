my_file = open("2_third_file.txt", "w+")
with open("first.txt") as f1, open("second.txt") as f2:
    first = f1.read().split('\n')
    second = f2.read().split('\n')
    for i,n in zip(first,second):
        each = i.split()
        one = n.split()
        my_file.write(each[0]+' '+one[0]+'\n')