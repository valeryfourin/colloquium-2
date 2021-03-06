'''
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 20 значеннями
    for i in range(20):
        a = random.randint(100, 200) # створимо значення рандомно
        A.append(a)
    print(f'Your array: {A}')

    E = [] # масив з парними числами
    sum_E = 0 # сума всіх парних чисел

    for i in range(20):
        if A[i]%2 == 0: # якщо остача від ділення числа на 2 = 0, тоді число є парним, записуємо його до масиву Е
            E.append(A[i])

    for i in E: # сумуємо всі елементи масиву Е, значення записуємо до змінної sum_E
        sum_E += i
    print(f'Even numbers: {E}')
    print(f'The summary of all even numbers: {sum_E}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться