contador = list()
cadastro = dict()

while True:
    valores = input('Digite o seu nome e depois o seu sexo: ').title().split()

    if len(valores) == 0:
        break
    else:
        nome, sexo = map(str, valores)

        for c in range(len(cadastro)+1):
            if c not in cadastro:
                cadastro[c] = {'nome': nome, 'sexo': sexo}
                if sexo == 'Feminino':
                    contador.append(0)
                elif sexo == 'Masculino':
                    contador.append(1)

print(f'O total de homens cadastrados foram: {contador.count(0)}\n'
      f'O total de mulheres cadastradas foram: {contador.count(1)}')
