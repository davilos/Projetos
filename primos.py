n = int(input('Quantidade de primos: '))

primos = list(filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, n+1)))

print(primos)
