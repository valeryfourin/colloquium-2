'''
Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 20 значеннями
    for i in range(20):
        a = round(random.uniform(50, 100), 2)
        # створимо дійсні числа рандомно за допомогою uniform() з модуля random
        # і округлимо до 2 знаків після коми з допомогою round()
        A.append(a)
    print(f'Your array: {A}')

    while True:
        try:
            num = float(
                input('Please input the desired number: '))  # число, з яким будуть порівнюватись елементи масиву А
            for i in A:
                if num not in A:
                    print('\nThere is no such number!')
                    break
                    # перевірка на наявність введеного числа у масиві, якщо немає, то виводться повідомлення про помилку
        except ValueError or TypeError:
            print(f'\nPlease input a float type number!')  # перевірка на відовідність типу введених користувачем даних
            continue
        break
        
    big_A = [] # числа більші за введене

    for i in A:
        if i > num:
            big_A.append(i) # якщо число задовольняє умову і більше за введене, то воно записується в масив big_A

    print(f'\nNumbers bigger than {num}: {big_A}')
    print(f'Sum of numbers bigger than {num}: {sum(big_A)}') # функція sum() повертає суму масиву

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться