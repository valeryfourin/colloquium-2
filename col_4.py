'''
Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
Виконала Новіцька В. І. 122Б
'''
sur = ['Turing', 'Eckert', 'Dijkstra', 'Edison', 'Lovelace']
let = 'E' # задання без необхідності введення
# let = input('Input first letter of the surname in capital: ') # введення користувачем
sur_picked = [] # в цей масив будуть записуватись фамілії, що починаються на певну літеру
for i in sur:
    if i[0] == let: # якщо за умовою перша літера фамілії додрівнює заданій, то додаємо цю фамілію у масив sur_picked
        sur_picked.append(i)
print(f'Surnames starting from letter {let}: {sur_picked}')