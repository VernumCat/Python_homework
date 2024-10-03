first = int(input('Введите целое число № 1: '))
second = int(input('Введите целое число № 2: '))
third = int(input('Введите целое число № 3: '))
if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)