'''
Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
Bиконала Новіцька В. І. 122Б
'''
import numpy as np
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = []  # масив з 10 значеннями
    for i in range(10):
        a = random.randint(-10, 10)  # заповнимо масив рандомними числами
        A.append(a)
    print()  # відступ для більшої читабельності виведених користувачеві даних
    print(f'Your array: {A}')

    while True:
        try:
            a = int(input('Please input a number: '))

        except ValueError or TypeError:  # перевірка на відповідність введеного числа умові
            print('\nPlease input an integer!')
            continue
        break

    t = False  # прапор, який зміниться на True, якщо в масиві знайдеться неповторюване максимальне число, не більше за а

    A_count = A.count(max(A))
    # функція count() показує к-ть входжень максимального числа в масиві. якщо воно більше за 1, то прапо залишиться False
    for i in range(len(A)):
        if (A_count == 1) and max(A) <= a:
            # перевірка на виконання двох умов: максимальне число входить у масив лише один раз
            # і воно не більше за введене користувачем число а, - якщо вони виконуються, прапор змінюється на True
            t = True


    if t == True:  # варіант, коли є неповторюване максимальне число, не більше за а
        print(f'\n{t}')
        print(f'Maximum number {max(A)} does not repeat in array A and it is not bigger than {a}')
    else:  # варіант, коли максимальне число повторюється або більше за а
        print(f'\n{t}')
        print(f'Array A has multiple maximum number or maximum number {max(A)} is bigger than {a}.')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break # програма завершиться