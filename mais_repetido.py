lista = list()

while True:
    nome = input('Digite o seu primeiro nome: ').title()

    if nome == '':
        break
    else:
        lista.append(nome)

mais_comum = max(lista, key=lista.count)

print(f'O nome mais comum na lista é {mais_comum}')
