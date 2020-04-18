'''
Дані про температуру води на Чорноморському узбережжі за декаду
вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
купання.
Bиконала Новіцька В. І. 122Б
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = [] # масив з 10 значеннями температур у вересні
    for i in range(10):
        a = random.randint(15, 25) # створимо значення температур рандомно
        A.append(a)
    print(f'Temperatures in September: {A}')
    count = 0 # кількість температур придатних для купання, нехай це буде >+20
    for i in A:
        if i >= 20: count += 1 # якщо у масиві знайдено температуру придатну для купання, у змінну count записується +1
    print(f'Number of days when water temperatures in September are acceptable for swimming (>+20): {count}')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться