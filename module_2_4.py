numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    for x in numbers[1:i]:
        if i % x == 0 and i != x:
            not_primes.append(i)
            break
    if i not in not_primes:
        primes.append(i)
print('Primes:', primes)
print('Not primes:', not_primes)

