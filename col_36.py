'''
Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
Bиконала Новіцька В. І. 122Б
'''
A = [2, -34, 12, 0, -2, 6, 45, -78, 9, -10] # масив з 10 значеннями
print(f'Your array: {A}')

B = [] # додатні числа

for i in A:
    if i > 0:
        B.append(i)
        # якщо число більше за нуль, тоді записуємо його до масиву В.

print(f'All positive integers in array A: {B}')
print(f'Sum of all positive integers: {sum(B)}') # функція sum() повертає суму елементів масиву

