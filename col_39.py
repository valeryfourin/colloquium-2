'''
Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.
Bиконала Новіцька В. І. 122Б
'''
A = [[5, 6], [-1, 3], [6, 5], [-2, 2], [1, 5], [-3, 3], [5, 2], [-4, 7], [1, 4], [-3, 2]]
# масив містить дані про 10 днів квітня, кожен день це список з двома значеннями: температура повітря і к-ть опадів у мм
print(f'Temperature and precipitation during 10 days of april: {A}')

A_rain = []  # запишемо сюди к-ть опадів у вигляді дощу
A_snow = []  # запишемо сюди к-ть опадів у вигляді снігу

for i in range(len(A)):
    if A[i][0] > 0:
        A_rain.append(A[i][1])
        # якщо температура повітря (перше значення масиву) більша за 0, то будемо вважати, що опадами є дощ
        # запишемо цю к-ть опадів (друге значення масиву) до змінної A_rain
    elif A[i][0] < 0:
        A_snow.append(A[i][1])
        # якщо температура повітря (перше значення масиву) менша за 0, то будемо вважати, що опадами є сніг
        # запишемо цю к-ть опадів (друге значення масиву) до змінної A_snow

print(f'\nRain precipitation (temperature bigger than 0 degrees): {sum(A_rain)} mm')
print(f'Snow precipitation (temperature less than 0 degrees): {sum(A_snow)} mm')