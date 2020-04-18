'''
Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
Bиконала Новіцька В. І. 122Б
'''
import numpy as np
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    B = np.array([4, 3, 12, 5, 2, 7, 8, 5 ,13, 7])
    print(f'Array B: {B}')

    while True:
        try:
            print()  # відступ для більшої читабельності виведених користувачеві даних
            a = int(input('Please input a desired number (for example 5 or 7 for this array to see how it works): '))

        except ValueError or TypeError:  # перевірка на відповідність введеного числа умові
            print('\nPlease input an integer!')
            continue
        break

    a_picked = 0  # в цій змінній зберігатиметься індекс першого зустрінутого числа рівного наперед заданому числу а

    B_even = []  # заведемо тестовий список, щоб побачити, які елементи програма розпізнала як парні
    for i in range(len(B)):
        if B[i] == a:
            a_picked = i
            # цикл знаходить перше число рівного наперед заданому числу а і записує його індекс до змінної a_picked
            break  # після першого знайденого такого числа програма припинить пошук

    for g in range(a_picked):
        if B[g] % 2 == 0: B_even.append(B[g])
        # якщо остача від ділення елементу масиву на 2 = 0, то він є парним, записуємо його до масиву В_even

    print(f'\nNumber of even elements in array В before the first {a}: {len(B_even)}')
    print(f'Even elements in array В before the first {a}: {B_even}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break # програма завершиться