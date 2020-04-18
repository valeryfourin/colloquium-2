'''
Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 15 значеннями
    for i in range(15):
        a = random.randint(10, 50) # створимо значення рандомно
        A.append(a)
    print(f'Your array: {A}')

    E = [] # масив з числами, кратними 7
    mult_E = 1 # добуток всіх чисел масиву кратних 7

    for i in range(15):
        if A[i]%7 == 0: # якщо остача від ділення числа на 7 = 0, тоді число є кратним 7, записуємо його до масиву Е
            E.append(A[i])

    for i in E: # множимо всі елементи масиву Е, значення записуємо до змінної mult_E
        mult_E *= i
    print(f'Numbers that can be divided by 7: {E}')
    print(f'The multiplication of all numbers that can be divided by 7: {mult_E}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break # програма завершиться