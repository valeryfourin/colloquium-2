'''
Введіть масив з 20 елементів і визначте, чи є в ньому елементи з однаковими значеннями.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = []  # масив з 20 значеннями
    for i in range(20):
        A.append(random.randint(0, 100))  # заповнимо масив рандомними числами
    print(f'Your array: \n{A}')

    B = []  # елементи, що повторюються більше одного разу
    for i in A:
        c = A.count(i)  # функція рахує к-ть повторів елементу, і, якщо вона більша за 1, додає його в масив  В
        if c != 1:
            B.append(i)

    if B == 0:  # жоден елемент не повторюються
        print('No number is repeated')
    else:
        for i in B:  # виводить елемент та к-ть разів, коли він повторився
            print(f'{i} is repeated {B.count(i)} times')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться