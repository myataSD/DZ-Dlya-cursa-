#Ввод значений 
cellX = int(input('Введите номер столбца (от 1 до 8): '))
cellY = int(input('Введите номер строки (от 1 до 8): '))

#Проверка условия, сложение X и Y и остаток от деления на 2
if 0 < cellX < 9 and 0 < cellY < 9: 
    if (cellX + cellY) % 2 == 0:
        print("NO")  # Клетка черная
    else:
        print("YES")   # Клетка белая
else:
    print('Вы ввели неправильное значение!!')