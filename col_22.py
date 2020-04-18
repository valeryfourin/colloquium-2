'''
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 10 значеннями
    for i in range(10):
        a = random.randint(5, 500) # заповнимо масив рандомними числами
        A.append(a)
    print(f'Your array: {A}')

    B = [] # числа кратні 3 і 9
    mult_B = 1 # добуток чисел кратних 3 і 9

    for i in range(10):
        if (A[i]%3 == 0) :
            B.append(A[i])
            # якщо остача від ділення числа на 3 дорівнює 0, тоді число записуємо до масиву В. умову про кратність 9 можемо
            # не враховувати, оскільки множина чисел кратних 9 входить у множину чисел кратних 3

    for i in B:
        mult_B *= i # множимо елементи масиву B

    print(f'Integers divisible by 3 and 9: {B}')
    print(f'Multiplication of all integers divisible by 3 and 9: {mult_B}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться