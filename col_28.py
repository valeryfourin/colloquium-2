'''
Знайти кількість парних елементів одновимірного масиву.
Bиконала Новіцька В. І. 122Б
'''
import numpy as np
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    while True:  # цикл перевіряє на виникнення помилки
        try:
            print()  # відступ для більшої читабельності виведених користувачеві даних
            n = int(input('Input number of elements:'))  # користувач вводить к-ть елементів
        except ValueError or TypeError:  # перевірка на відповідність введеної цифри умові
            print('\nPlease input an integer!')
            continue
        break

    A=np.zeros((n), dtype = int)  # створюємо масив А і заповнюємо його нулями

    for i in range(n):  # генеруємо елементи масиву А
        A[i] = random.randint(-10,10)
    print(f'Array A: {A}')

    A_even = []  # парні елементи одновимірного масиву А
    for i in A:
        if i % 2 == 0: A_even.append(i)
        # якщо остача від ділення елементу масиву на 2 = 0, то він є парним, записуємо його до масиву A_even
    print(f'Number of even elements in array A: {len(A_even)}')
    print(f'Even elements in array A: {A_even}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break # програма завершиться