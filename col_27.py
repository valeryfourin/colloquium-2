'''
Лінійний масив містить відомості про кількість опадів, що випали за
кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
Bиконала Новіцька В. І. 122Б
'''
P = [35, 47, 29, 32, 45, 39, 36, 27, 28, 31, 41, 42] # опади за кожен з 12 місяців
sum_P = sum(P) # сума всіх опадів за 12 місяців, сума елементів масиву Р
dry_P = list(filter(lambda x: x < 30, P))  # опади менші за 30 мм
num_dry_P = len(dry_P)  # к-ть місяців з опадами меншими за 30 мм
min_dry_P = min(dry_P)  # найпосушливіший місяць року
# за допомогою filter() запишемо у змінну dry_P всі елементи нижчі 30, використаємо lambda, замість def для простоти коду
av_P = sum_P/len(P)  # середнє значення, сума елементів масиву ділиться на їх кількість
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
S = dict(zip(P, month))  # утворюється словник, де ключем є к-ть опадів, а значенням є відповідний їй місяць
print(f'List of precipitations and months: \n{S}')
print(f'General amount of precipitation aroung the year: {sum_P}')
print(f'Average amount of precipitation: {av_P}')
print(f'Number of dry months (precipitation less than 30 mm): {num_dry_P} months:')
for i in dry_P:
    print(f'{S[i]}: {i}mm')  # цикл виводить посушливий місяць по ключу зі словника S
print(f'The most dry month of a year: {S[min_dry_P]}: {min_dry_P}mm')

