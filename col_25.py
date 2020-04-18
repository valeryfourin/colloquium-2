'''
Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до 100.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 10 значеннями
    for i in range(10):
        a = random.randint(10, 100) # заповнимо масив рандомними числами
        A.append(a)
    print(f'Your array: {A}')

    B = [] # числа кратні 5
    mult_B = 1 # добуток чисел кратних 5

    for i in A:
        if i%5 == 0:
            B.append(i)
            # якщо остача від ділення числа на 5 дорівнює 0, тоді число записуємо до масиву В.

    for i in B:
        mult_B *= i # множимо елементи масиву B

    print(f'Integers divisible by 5: {B}')
    print(f'Multiplication of all integers divisible by 5: {mult_B}')

    answer = input('Do you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться