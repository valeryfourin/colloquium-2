'''
Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
Bиконала Новіцька В. І. 122Б
'''
import random
A = [] # масив з 7 рандомними елементами
for i in range(1, 8):
    a = random.randint(-10, 10)
    A.append(a)
print(f'Your array: \n{A}')
for i in range(7):
    A[i] = A[i] * 2 # кожен елемент масиву А множиться на 2
print(f'Your array with elements multiplied by 2: \n{A}')