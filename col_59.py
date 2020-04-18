'''
Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних чисел в ньому.
Bиконала Новіцька В. І. 122Б
'''
import random
import numpy as np
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    print()  # відступ для більшої читабельності виведених користувачеві даних
    A = np.zeros((10), dtype=int)  # створимо масив з 10 нулями
    for i in range(10):
        A[i] = random.randint(0, 10)  # заповнимо масив рандомними числами
    print(f'Your array: \n{A}')

    A_1 = []
    for i in range(len(A)-1):
        if A[i] not in A_1:
            A_1.append(A[i])  # до масиву A_1 буде додаватись елемент масиву А за умови, що його там ще немає
        else: continue  # якщо елемент масиву А вже є в масиві A_1, він додаватись не буде

    print(f'\nNumber of different integers in array A is {len(A_1)}: \n{np.array(A_1)}')


    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться