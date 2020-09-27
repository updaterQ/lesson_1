second_in_day = 86400
second_in_hour = 3600
minutes_in_hour = 60
second_in_minute = 60

while True:
    user_input = input('Введите время в секундах: ')
    if user_input.isalpha():
        print('Необходимо вводить только цифры')
    elif int(user_input) > second_in_day:
        print(f'В стуках {second_in_day} секунд. Пожалуйста, введите корректные данные')



    else:
        user_input = int(user_input)
        hours = user_input // second_in_hour
        minutes = (user_input % second_in_hour) // minutes_in_hour
        seconds = (user_input % second_in_hour) % second_in_minute
        print(f'Время:{hours}:{minutes}:{seconds}')
        break