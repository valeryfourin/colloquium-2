'''
Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м.
Bиконала Новіцька В. І. 122Б
'''
import numpy as np
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    print()  # відступ для більшої читабельності виведених користувачеві даних
    A = []  # масив з 30 значеннями довжин опор
    for i in range(30):
        a = random.randint(0, 20)  # заповнимо масив рандомними числами
        A.append(a)
    print(f'Your array: {A}')

    while True:
        try:
            r = int(input('Please input radius (must be >0 and divisible by 5): '))
            if r < 0:
                print('\nInputed number must be more than 0!')
                continue
            elif r % 5 != 0:
                print('\nInputed number must be divisible by 5!')
                continue
        except ValueError or TypeError:  # перевірка на відповідність введеного числа умові
            print('\nPlease input an integer!')
            continue
        break

    A_col = []  # масив зі всіма довжинами опор, розташованими на відстані r / 5 один від одного

    for i in range(0, len(A), int(r/5)):  # цикл додає у масив A_col довжини опор, розташованих на відстані r / 5
        A_col.append(A[i])
    print(f'Length of the supportive columns placed at a distance {int(r / 5)}: \n{A_col}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться