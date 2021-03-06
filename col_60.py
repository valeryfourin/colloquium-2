'''
Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число однакових чисел, що йдуть підряд в ньому.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    print()  # відступ для більшої читабельності виведених користувачеві даних
    A = []  # створимо масив з 10 значеннями
    for i in range(10):
        A.append(random.randint(0, 3))  # заповнимо масив рандомними числами
    print(f'Your array: \n{A}')

    max_count = 0  # максимальна к-ть однакових значень підряд
    c = 0  # к-ть однакових значень підряд

    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            c += 1  # кожного разу як знаходяться два однакових числа, до змінної с додається +1
        if A[i] != A[i + 1]:  # якщо елемент не дорівнює натупному, отже однакові числа, що йшли підряд закінчились
            if max_count <= c:
                max_count, c = c, 0
                # якщо змінна  max_count менша за с, то їй надається значення с, а с обнуляється,
                # і вона знову починає пошук елементів, що йдуть підряд

    if max_count == 0:
        print(f'No same integers in a row.')
    else:
        print(f'\nMax number of the same integers in a row in array A is {max_count+1} times')
        # count показує к-ть порівнянь, тобто к-ть однакових елементів завжди на 1 більша

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться