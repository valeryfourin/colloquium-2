'''
Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 10 значеннями
    for i in range(10):
        a = random.randint(-100, 100) # створимо значення рандомно
        A.append(a)
    print(f'Your array: {A}')
    print(f'Min value: {min(A)}') # функція min() повертає найменше значення масиву

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться