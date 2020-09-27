user_input = int(input('Ведите целое положительное число: '))
ls = []
while user_input > 10:
    ls.append(user_input % 10)
    user_input //= 10
max_number = max(ls)
print(f'Максимальне число {max_number}')