marks = []
a = [5,4,3,2]
while 1:
    mark = int(input())
    if mark == 0 : break
    elif mark in a :
        marks.append(mark)
    else: print('error')

print((len(marks) - marks.count(2))/len(marks)*100)