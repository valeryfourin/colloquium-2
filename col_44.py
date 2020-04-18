'''
Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
Bиконала Новіцька В. І. 122Б
'''
import numpy as np
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = []  # масив з 30 значеннями
    for i in range(30):
        a = random.randint(0, 20)  # заповнимо масив рандомними числами
        A.append(a)
    print(f'Your array: {A}')

    A_cond = []  # масив з елементами, для яких виконується умова: збігається зі своїм номером і при цьому кратний 3

    for i in range(len(A)):
        if (A[i] == i) and (A[i] % 3 == 0):
            # якщо для елементу виконується умова: збігається зі своїм номером і при цьому кратний 3
            # то він записується до змінної A_cond
            A_cond.append(A[i])

    print(f"\nNumber of integers for which the condition 'element is equal to its index and is divided by 3' is fulfilled: {len(A_cond)}")
    print(f"Integers for which the condition 'element is equal to its index and is divided by 3' is fulfilled: {A_cond}")
    print("\nIf you haven't received the desired result, try again.")

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться

