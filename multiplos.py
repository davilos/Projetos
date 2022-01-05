valores = input('Valores: ').split()
mult = list()

for x in range(int(valores[0]), int(valores[1])+1):
    if not x % int(valores[2]):
        mult.append(x)

print(f'Os múltiplos de {valores[2]} de {valores[0]} até {valores[1]} são {mult}')
