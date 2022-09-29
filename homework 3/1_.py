with open('1_file.txt', 'r') as the_file:
    students = the_file.read().split('\n')

my_file = open("1_new file.txt", "w+")
for i in students:
    each = i.split()
    each[0] = each[0].capitalize()
    each[1] = each[1].capitalize()
    each[3] = '8708'+ each[3]+' '+each[4]
    my_file.write(each[0] +' '+ each[1] +' '+ each[2] +' '+ each[3]+'\n')
    