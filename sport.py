ferst_day = int(input('Введите сколько вы пробежали в первый день: '))
target = int(input('Введите сколько вы хотите пробежать: '))
day = 1
while target - ferst_day > 0:
    ferst_day = ferst_day + (ferst_day * 0.1)
    day += 1
print(f'Вы достигните своей цели на {day}-й день')