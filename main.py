
"""Сортировка пузырьком"""
mas = [-4, 0, 1, 10, 12, 9, -10]
n = len(mas)
# Список всех чисел введенных с экрана
count = 0
# Счетчик замен
while True:
    if n == len(mas):
        for run in range(n-1):
            for i in range(n-1):
                if mas[i] > mas[i + 1]:
                    mas[i], mas[i+1] = mas[i+1], mas[i]
                    count += 1
        break
    else:
        print('ValueError')
        n = int(input())
        mas = list(input().split())

print(f'Отсортированные массив пузырьком = {mas}')
print(f'Всего было сделано: {count}')


"""Сортировка выбором"""
a = [-4, 0, 1, 10, 12, 9, -10]    # Массив
n = len(a)    # Длинна массива

for i in range(n-1):    # Перебор элемент с 0 индекса до конца - 1
    m = a[i]  # Минимальное значение в массиве
    p = i   # Индекс минимального значения в массиве

    for j in range(i+1, n):
        if m > a[j]:
            m = a[j]
            p = j
    # Замена элементов
    if p != i:
        t = a[i]
        a[i] = a[p]
        a[p] = t

print(f'Отсортированные массив выборкой = {a}')


"""Сортировка вставкой"""
b = [-4, 0, 1, 10, 12, 9, -10]  # Массив
n = len(b)

for i in range(1, n):
    for j in range(i, 0, -1):
        if b[j] < b[j-1]:
            b[j], b[j-1] = b[j-1], b[j]
        else:
            break
print(f'Отсортированные массив вставкой = {b}')


# Функция слияния двух отсортированных списков
def merge_list(a, b):
    c = []
    n = len(a)
    m = len(b)

    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


# Функция деления списка и слияния списков в общий отсортированный список
def split_and_merge_list(a):
    n1 = len(a) // 2
    a1 = a[:n1]
    a2 = a[n1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)


a = [-4, 0, 1, 10, 12, 9, -10]
a = split_and_merge_list(a)

print(f'Отсортированные список быстрой сортировкой {a}')
