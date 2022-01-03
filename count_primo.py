def contador_de_primos(n):
    for x in range(2, n // 2 + 1):
        if not n % x:
            return 0
    return 1


num_primos = 0

for l in range(2, 12):
    num_primos += contador_de_primos(l)

print(num_primos)
