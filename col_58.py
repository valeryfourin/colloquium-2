'''
Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому повторюється найчастіше число.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    print()  # відступ для більшої читабельності виведених користувачеві даних
    A = []  # масив з 30 значень
    for i in range(100):
        a = random.randint(0, 50)  # заповнимо масив рандомними числами
        A.append(a)
    print(f'Your array: \n{A}')

    count = 0  # к-ть однакових значень підряд
    A_1 = 0

    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            count += 1
            A_1 = A[i]  # збережемо в змінну A_1 це значення, що повторюється

    if A_1 == 0:
        print(f'Every element is repeated 1 time')
    else:
        print(f'The most repeated element {A_1} was repeated {count+1} times')
        # count показує к-ть порівнянь, тобто к-ть однакових елементів завжди на 1 більша

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться