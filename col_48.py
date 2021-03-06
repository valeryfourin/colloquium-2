'''
Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
з початку і третього від кінця і т.д.
Bиконала Новіцька В. І. 122Б
'''
print()  # для читабельності коду
A = ['Libertex', 'NPBFX', 'Alpari', 'Intrade', 'Forex', 'AMarkets']  # приклад масиву з парною к-тю елементів
B = ['Libertex', 'NPBFX', 'Alpari', 'Intrade', 'Forex']  ## приклад масиву з НЕпарною к-тю елементів

print(f'Array A: {A}')
print(f'Array B: {B}')

def switch(A):
    '''
    створимо функцію, яка буде змінювати місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
    з початку і третього від кінця і т.д.
    '''
    if len(A) % 2 == 0:  # варіант, коли к-ть елементів масиву парна
        A_mid = len(A) // 2  # центральний елемент масиву
        i = 0  # лічильник, який буде зібльшуватись від першого елемента до центрального
        j = len(A) - 1  # лічильник, який буде зібльшуватись від останнього елемента до центрального
        while i < A_mid and j > A_mid:
            A[i], A[j] = A[j], A[i]  # протилежні відносно центрального елементи міняються місцями
            i += 1  # крок +1 до центрального елемента
            j -= 1  # крок -1 до центрального елемента
        A[A_mid], A[A_mid - 1] = A[A_mid - 1], A[A_mid]
        # оскільки к-ть елементів парна, то 2 центральні елементи також потрібно поміняти місцями
        print(f'\nSymmetrically reflected (even length of array): \n{A}')

    else:
        # варіант, коли к-ть елементів масиву НЕпарна, принцип роботи той самий, що і в попередньому варіанті,
        # тільки центральний елемент один і його не потрібно переставляти
        A_mid = len(A) // 2
        i = 0
        j = len(A) - 1
        while i < A_mid and j > A_mid:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        print(f'\nSymmetrically reflected (odd length of array): \n{A}')


switch(A)
# викличемо функцію для першого масиву, щоб побачити, як програма змінить місцями елементи парного масиву
switch(B)
# викличемо функцію для другого масиву, щоб побачити, як програма змінить місцями елементи НЕпарного масиву