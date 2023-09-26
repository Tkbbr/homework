marks = input('Введите оценки через пробел: ')

print('У вас', marks.count('5'), 'пятёрок')
print('У вас', marks.count('5')/(len(marks)-marks.count(' '))*100 ,'процентов пятёрок')

