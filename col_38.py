'''
Дані про направлення вітру (північний(north), південний(south), східний(east), західний(west)) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с.
Bиконала Новіцька В. І. 122Б
'''
A = [['south', 6], ['west', 9], ['south', 10], ['north', 2], ['east', 5], ['south', 3], ['west', 12], ['north', 7], ['south', 14], ['east', 7]]
# масив містить дані про 10 днів листопада, кожен день це список з двома значеннями: направлення і швидкість у м/с

A_south = []  # запишемо сюди всі дні коли дув південний вітер
for i in range(len(A)):
    if A[i][0] == 'south':
        A_south.append(A[i])
        # якщо перше значення списку є південь (south) (у кожному списку першим значенням є направлення вітру),
        # то запишемо цей список до змінної A_south

A_south_b = []  # запишемо сюди всі дні коли дув південний вітер зі швидкістю, більшою за 8 м/с
for i in range(len(A_south)):
    if A_south[i][1] > 8:  # якщо швидкість вітру (другий елемент списку, індекс 1) більша за 8 м/с, додаємо у масив A_south_b
        A_south_b.append(A_south[i])

print(f'Days with a southern wind: \n{A_south}')
print(f'\nDays with a southern wind bigger than 8 m/s: {len(A_south_b)} days: \n{A_south_b}')
