count_m, count_f = 0, 0
cadastro = dict()

while True:
    valores = input('Digite o seu nome e depois o seu sexo: ').title().split()

    if len(valores) == 0:
        break
    else:
        nome, sexo = valores

        for c in range(len(cadastro)+1):
            if c not in cadastro:
                cadastro[c] = {'nome': nome, 'sexo': sexo}
                if sexo == 'Feminino':
                    count_f += 1
                elif sexo == 'Masculino':
                    count_m += 1

print(f'O total de homens cadastrados foram: {count_m}\nO total de mulheres cadastradas foram: {count_f}')
