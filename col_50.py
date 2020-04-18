'''
У лотереї розігрувалося 100 квитків.
Таблиця містить 10 номерів виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
'''
import random
while True:  # програма знаходиться в циклі, який буде виконуватись за умови, що користувач хоче виконати її знову
    A = []  # масив з 100 номерами лотерейних квитків
    for i in range(100):
        A.append(random.randint(0, 100))  # заповнимо масив рандомними числами
    print(f'Lottery tickets: \n{A}')

    B = []  # масив з 10 номерами виграшних лотерейних квитків вибраних з масиву А за допомогою функції choice()
    for i in range(10):
        B.append(random.choice(A))
    # print(B) # можна вивести масив з виграшними квитками, щоб протестувати програму і побачити, що вона виведе у випадку виграшу

    N = int(input('Choose your ticket: '))  # користувач вибирає квиток

    if N in B:  # якщо номер вибраного квитка є в масиві з виграшними квитками, виводиться повідомлення, що вибраний квиток є виграшним
        print(f'Congratulations! {N} is a winning ticket.')
    else:  # якщо номер вибраного квитка відсутній в масиві з виграшними квитками, виводиться повідомлення про це
        print(f'Sorry. {N} is not a winning ticket :(')

    answer = input('\nDo you want to try again? Yes-1, No-2:')
    if answer == '1':
        continue  # програма виконається знову
    else:
        break  # програма завершиться
