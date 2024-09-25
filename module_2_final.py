N = int(input('Какое число ты видишь на камне? '))
all_N = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = list()
if N in all_N:
    dividers = list()
    for div in range(3, N+1):
        if N % div == 0:
            dividers.append(div)
    for i in range(1, N//2+1):
        for div in dividers:
            if i != div - i and i <= div//2:
                result.append([i, div-i])
    print('Чтобы выбраться введи эти пары:', *result)
else:
    print('Ты ошибся, посмотри внимательнее!')
