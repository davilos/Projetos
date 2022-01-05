def contador_de_primos(n):
    for x in range(2, n // 2 + 1):
        if not n % x:
            return 0
    return 1


num_primos = 0

# Opção 1 de input:
# a, b = [int(input(f'Valor {_+1}: ')) for _ in range(2)]

# Opção 2 de input:
valores = input('Valores: ').split()
x = list(map(int, valores))

for l in range(x[0], x[1]):
    num_primos += contador_de_primos(l)

print(f'Os números primos existentes entre {x[0]} e {x[1]} é {num_primos}')