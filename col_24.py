'''
Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 30 значеннями
    for i in range(30):
        a = random.randint(500, 1000) # заповнимо масив рандомними числами
        A.append(a)
    print(f'Your array: {A}')

    B = [] # числа кратні 5 і 8

    for i in A:
        if (i%5 == 0) and (i%8 == 0):
            B.append(i)
            # якщо остача від ділення числа на 5 і 8 дорівнює 0, тоді число записуємо до масиву В.

    print(f'Integers divisible by 5 and 8: {B}')
    print(f'Multiplication of all integers divisible by 5 and 8: {sum(B)}') # функція sum() повертає суму елементів масиву

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться