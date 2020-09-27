revenue = int(input('Введите доход: '))
damages = int(input('Введите издержки: '))
human_resorce = int(input('Введите колличество рабочих в фирме:'))
print(f'Издержки составили: {damages}\nПрибыль составила: {revenue}')
income = revenue - damages
profit_per_employee = income // human_resorce
profitability = (revenue / damages) * 100
if revenue > damages:
    print(f'Ваша компания в прибыли на {income}')
    print(f'Рентабельность предприятия составляет: {profitability}%')
    print(f'Прибыль на каждого сотрудника фирмы составляет:{profit_per_employee}')
else:
    print(f'У вас финаносовые трудности. Расходы привышают доходы на {income}')