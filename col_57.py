'''
Відомість на зарплату представлена як дві таблиці. Одна містить прізвища працівників цеху,
а друга - їх зарплату за поточний місяць. Знайдіть прізвище працівника, зарплата якого найменш відхиляється
від середньої зарплати всіх працівників за поточний місяць. Знайдіть прізвища двох працівників з
найбільшою заробітною платою. Видаліть з відомості на зарплату відомості про працівника, зарплата якого мінімальна.
Bиконала Новіцька В. І. 122Б
'''
surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Davis', 'Miller', 'Wilson', 'Rogers', 'Ross', 'Henderson']
salaries = [1500, 900, 1250, 1100, 890, 740, 1360, 1600, 670, 1090]
workers = list(zip(surnames, salaries))  # масив з робітниками та їхніми зарплатами
print(f'List of workers and their salaries: \n{workers}')

av_s = sum(salaries)/len(salaries) # середня зарплата
print(f'\nAverage salary: {av_s}')

surnames_in = []  # індекси зарплат, найближчих до середньої (відхилення від середньої межах від -10 до 10)
for i in range(len(salaries)):
    if (salaries[i] - av_s) in range(-10,10):
        surnames_in = i
        # якщо різниця зарплати працівника від середньої лежить в межах від -10 до 10, то додамо її індекс до surnames_in

print(f'Salary closest to average: {workers[surnames_in]}')

salary_max = salaries.index(max(salaries))  # індекс максимальної зарплати
salary_second_max = 0  # індекс другої максимальної зарплати

for i in range(len(salaries)):
    if salary_max > salaries[i] > salary_second_max:
        salary_second_max = i
        # знайдемо другий максимальний елемент скориставшись таким принципом: якщо об'єкт ітерації менший
        # за максимальний і більший за той, який в змінній salary_second_max, то цій змінній присуджуємо індекс цього
        # об'єкта і, таким чином, до кінця циклу знайдемо другий максимальний елемент

max_salaries = []  # змінна зі значеннями 'працівник зарплата'
for i in (salary_max, salary_second_max):
    max_salaries.append(workers[i])

print(f'Two biggest salaries: {max_salaries}')

for i in range(len(workers)):
    if workers[i][1] == min(salaries):
        del workers[i]  # видалимо зі списку елемент значення, якого дорівнює найменшій зарплаті
        break

print(f'List of workers and their salaries without minimum salary ({min(salaries)}): \n{workers}')