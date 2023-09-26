surname = input()
profession = input()
students = []
while 1 :
    group = int(input())
    if group == 0 : break
    else: students.append(group)

resoult = []
resoult.append(surname)
resoult.append(profession)
resoult.insert(2,students)
print(resoult)