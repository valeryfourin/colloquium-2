'''
Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
Bиконала Новіцька В. І. 122Б
'''
import numpy as np
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = []  # масив з 30 значеннями
    for i in range(30):
        a = random.randint(-100, 100)  # заповнимо масив рандомними числами
        A.append(a)
    print(f'Your array: {A}')

    while True:
        try:
            print()  # відступ для більшої читабельності виведених користувачеві даних
            a = int(input('Please input number a>0: '))
            b = int(input('Please input number b>0: '))
            if a < 0 or b < 0:
                print('\nInputed number must be more than 0!')
                continue
        except ValueError or TypeError:  # перевірка на відповідність введеного числа умові
            print('\nPlease input an integer!')
            continue
        break

    A_cond = []  # масив з елементами, для яких виконуються умови: кратний а і не кратний b
    w = False  # зміниться на True, якщо знайдеться хоча б один елемент кратний а і не кратний b

    for i in A:
        if (i % a == 0) and (i % b != 0):
            # якщо для елементу виконується умова: кратний а і не кратний b, то він записується до змінної A_cond,
            # а прапор змінюється на True
            A_cond.append(i)
            w = True

    if w == True:  # знайшовся хоча б один елемент кратний а і не кратний b
        print()
        print(w)
        print(f'Elements that fulfill the condition: is divisible by {a} and not divisible by {b}: {A_cond}')
    else:  # не знайшовся жоден елемент кратний а і не кратний b
        print()
        print(w)
        print(f"Elements that fulfill the condition: is divisible by {a} and not divisible by {b} weren't found.")

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться
