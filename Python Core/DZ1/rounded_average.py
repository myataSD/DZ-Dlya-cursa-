#Ввод чисел
num1 = float(input("Введите 1 число: "))
num2 = float(input("Введите 2 число: "))

#Среднее арифметическое
avg  = (num1 + num2) / 2

#Округление среднего арифметического, до целого числа
rounded_avg = round(avg)

#Вывод округленного среднего арифметического
print(f"Среднее арифметическое чисел {num1} и {num2} равно {rounded_avg}")