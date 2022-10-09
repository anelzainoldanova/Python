def find_name(input_name): 
    students = open("namelist.txt", "r", encoding = "utf-8").read().split("\n") 
    list = [] 
    for student in students: 
        fullname = student.split("\t")[-1] 
        name = fullname.split() 
        if input_name == name[0][0] + name[-1][0]: list.append(fullname) 
        elif len(name) == 3 and input_name == name[0][0] + name[1][0] + name[-1][0]: list.append(fullname) 
    return list 
list_of_students = find_name(input("Enter the first letters of the student's full name:").upper()) 
if len(list_of_students): [print(student) for student in list_of_students] 
else: print("There is no such student on the list.")