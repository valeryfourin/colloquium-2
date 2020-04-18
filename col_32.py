'''
Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
Bиконала Новіцька В. І. 122Б
'''
import random
import numpy as np
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    while True:  # цикл перевіряє на виникнення помилки
        try:
            print()  # відступ для більшої читабельності виведених користувачеві даних
            n = int(input('Input number of elements in your array:'))  # користувач вводить к-ть елементів
        except ValueError or TypeError:  # перевірка на відповідність введеної цифри умові
            print('\nPlease input an integer!')
            continue
        break

    A = np.zeros((n), dtype=int)  # створюємо масив А і заповнюємо його нулями
    for i in range(n):  # генеруємо елементи масиву А
        A[i] = random.randint(-5, 5)
    print(f'Array A: {A}')

    t = False  # прапор, який зміниться на True, якщо в масиві знайдеться хоча б одне від’ємне і парне число

    A_1 = []  # заведемо тестовий список, щоб побачити, які елементи програма розпізнала як парні від'ємні
    for i in A:
        if i % 2 == 0 and i < 0:  # якщо елемент масиву менше нуля і парний, то прапор змінюється на True
            A_1.append(i)
            t = True

    if t == True:  # варіант, коли є хоча один парний від'ємний елемент
        print(f'\n{t}')
        print(f'Array A has at least one negative and even number: \n{A_1}')
    else:  # варіант, коли немає навіть одного парного від'ємного елемента
        print(f'\n{t}')
        print('Array A has no number that is negative and even simultaneously.')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться