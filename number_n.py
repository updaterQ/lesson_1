n = int(input("Введите число n: "))
temp = str(n)
temp1 = temp + temp
temp2 = temp + temp + temp
comp = n + int(temp1) + int(temp2)
print(temp1)
print(temp2)
print("Результат равен:", comp)