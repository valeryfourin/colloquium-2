'''
Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 20 значеннями
    for i in range(20):
        a = random.randint(150, 300) # створимо значення рандомно
        A.append(a)
    print(f'Your array: {A}')

    av_A = sum(A)/len(A) # змінна з середнім арифметичним масиву А, сума елементів ділиться на їх кількість
    B = [] # масив з елементами меншими за середнє арифметичне значення масиву

    for i in A:
        if i < av_A:
            B.append(i)
    print(f'\nElements smaller than arithmetic mean ({av_A}) of array A: {B}')
    print(f'Sum of elements smaller than arithmetic mean of array A: {sum(B)}') # функція sum() повертає суму елементів масиву

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться