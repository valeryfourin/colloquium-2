'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    while True:  # цикл перевіряє на виникнення помилки
        try:
            print()  # відступ для більшої читабельності виведених користувачеві даних
            n = int(input('Input number of elements in your array:'))  # користувач вводить к-ть елементів
        except ValueError or TypeError:  # перевірка на відповідність введеної цифри умові
            print('\nPlease input an integer!')
            continue
        break

    A = []  # створюємо масив А і заповнюємо його нулями
    for i in range(n):  # генеруємо елементи масиву А
        A.append(random.randint(-5, 5))
    print(f'Array A: {A}')

    for i in range(len(A)):  # врахуємо два випадки: якщо найменший елемент на останній позиції і якщо в середині масиву
        if A.index(min(A)) == -1:
            print(f"The minimum element of the array is on the last position, so we can't evaluate the arithmetic mean. ")
        else:
            sub_A = []  # елементи одновимірного масиву А, що стоять після мінімального значення цього ж масиву

            for i in range(A.index(min(A))+1, len(A)):  # цикл додає у масив sub_A всі елементи після мінімального і до кінця
                sub_A.append(A[i])

            av_sub_A = sum(sub_A)/len(sub_A)  # середнє арифметичне масиву sub_A, сума усіх елементів ділиться на їх к-ть

            print(f'\nThe arithmetic mean of all elements in array A after the first minimum element {min(A)}: {av_sub_A}')
            print(f'All elements in array A after the first minimum element {min(A)}: {sub_A}')
            break

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break # програма завершиться