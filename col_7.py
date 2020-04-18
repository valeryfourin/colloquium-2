'''
Створіть масив А [1..12] за допомогою генератора випадкових чисел з
елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
масиву числом 0.
Bиконала Новіцька В. І. 122Б
'''
import random
A = [] # масив з 12 рандомними елементами
for i in range(1, 13):
    a = random.randint(-20, 10)
    A.append(a)
print(f'Your array: \n{A}')
for i in range(12):
    if A[i] < 0:
        A[i] = 0 # якщо у масиві знайдено елемент менший за 0, то він замінюється нулем
print(f'Your array without negative elements: \n{A}')