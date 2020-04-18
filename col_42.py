'''
Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
Bиконала Новіцька В. І. 122Б
'''
import numpy as np
import random
import math

while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = []  # масив з 30 значеннями
    for i in range(30):
        a = random.randint(-1000, 1000)  # заповнимо масив рандомними числами
        A.append(a)
    print(f'Your array: {A}')

    A_cond = []  # масив з елементами, для яких виконується умова i*i<ai<i!

    for i in range(len(A)):
        if i*i < A[i] < math.factorial(i):
            # якщо для елементу виконується умова: значення елементу більше за квадрат його індексу
            # і менше за факторіал індексу, то він записується до змінної A_cond
            A_cond.append(A[i])

    print(f'\nNumber of integers for which the condition i*i<A[i]<i! is fulfilled: {len(A_cond)}')
    print(f'Integers for which the condition i*i<A[i]<i! is fulfilled: {A_cond}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться
