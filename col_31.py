'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
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

    sub_A = []
    # заведемо тестовий список, щоб побачити, які елементи програма розпізнала як ті, що належать інтервалу від -2 до 10

    for i in A:  # цикл додає у масив sub_A всі елементи, які потрапляють в інтервал від -2 до 10
        if i in range(-2, 11):
            sub_A.append(i)

    av_sub_A = sum(sub_A)/len(sub_A)  # середнє арифметичне масиву sub_A, сума усіх елементів ділиться на їх к-ть

    print(f'\nThe arithmetic mean of all elements in array A that stand within interval [-2, 10]: {av_sub_A}')
    print(f'All elements in array A that stand within interval [-2, 10]: {sub_A}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break # програма завершиться