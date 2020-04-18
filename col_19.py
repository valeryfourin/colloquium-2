'''
Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 200 до 300.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 20 значеннями
    for i in range(20):
        a = random.randint(200, 300)
        A.append(a)
    print(f'Your array: {A}')

    B = [] # числа, в яких остача від ділення на 2 дорівнює 3

    for i in range(20):
        if A[i]%2 == 3: # якщо остача від ділення числа на 2 дорівнює 3, тоді число записуємо до масиву В
            B.append(A[i])

    print(f'Integers with the remainder of the division by 2 is 3: {B}')
    print(f'The summary of all integers with the remainder of the division by 2 is 3: {sum(B)}') # функція sum() повертає суму масиву
    print(f"\n(The result is 0 because a remainder of division cannot be greater than divisor (3>2))")
    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break # програма завершиться