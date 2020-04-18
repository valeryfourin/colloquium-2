'''
Напишіть програму аналізу значень температури хворого за добу:
визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
температури виробляються шість раз на добу і результати вводяться з клавіатури у масив T.
Bиконала Новіцька В. І. 122Б
'''
T = [36.9, 38.1, 37.7, 37.9, 38.5, 36.8]

print(f'Temperatures: {T}')
T_max = max(T)  # функція повертає максимальне значення масиву
T_min = min(T)  # функція повертає мінімальне значення масиву
T_av = sum(T)/len(T)  # середнє значення, сума елементів масиву ділиться на їх кількість

print(f'\nMaximum temperature: {T_max}')
print(f'Minimum temperature: {T_min}')
print(f'Average temperature: {T_av}')