'''
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
Bиконала Новіцька В. І. 122Б
'''
import random
import numpy as np
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову

    print()  # відступ для більшої читабельності виведених користувачеві даних
    A = np.zeros((20), dtype=int)  # створюємо масив А з 20 елементів і заповнюємо його нулями
    for i in range(20):  # генеруємо елементи масиву А
        A[i] = random.randint(-10, 10)
    print(f'Array A: {A}')

    A_nonzero = []  # заведемо тестовий список, щоб побачити, які елементи програма розпізнала як ненульові
    for i in A:
        if i != 0:
            A_nonzero.append(i)  # елемент додається до списку A_nonzero, якщо він не дорівнює 0

    A_mult = 1
    for i in A_nonzero:
        A_mult *= i  # до масиву A_mult записується значення помножених всіх елементів списку A_nonzero

    print(f'\nThe multiplication of all non-zero elements of array A: {A_mult}')
    print(f'All non-zero elements of array A: {A_nonzero}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться