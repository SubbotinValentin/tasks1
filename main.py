"""Сортировка пузырьком"""
n = int(input())
# На вход подаем количество
mas = list(input().split())
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
        print(f'{mas}\n Всего было сделано: {count}')
        break
    else:
        print('ValueError')
        n = int(input())
        mas = list(input().split())
