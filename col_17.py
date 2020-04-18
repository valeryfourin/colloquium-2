'''
Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 20 значеннями
    for i in range(20):
        a = random.randint(100, 200) # створимо значення рандомно
        A.append(a)
    print(f'Your array: {A}')

    B = [] # числа з непарними номерами

    for i in range(20):
        if i%2 != 0: # якщо остача від ділення числа на 2 не дорівнює 0, тоді число є непарним, записуємо його до масиву В
            B.append(A[i])

    print(f'Integers with not even indexes: {B}')
    print(f'The summary of all integers with not even indexes : {sum(B)}') # функція sum() повертає суму масиву
    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break # програма завершиться
