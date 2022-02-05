import os
import random

matriz = [[random.randint(0, 30) for c in range(4)] for l in range(4)]

while True:
    print('MENU DE OPÇÕES')
    print('=' * 15)
    print('[1] Mostrar a Matriz')
    print('[2] Diagonal Principal')
    print('[3] Triângulo Superior')
    print('[4] Triângulo Inferior')
    print('[5] Sair')
    opcao = int(input('===== Opção: '))

    if opcao == 1:
        os.system("cls")
        for l in range(4):
            for c in range(4):
                print(f'[{matriz[l][c]:^5}]', end='')

            print()

    elif opcao == 2:
        os.system("cls")
        for l in range(4):
            for c in range(4):
                print(end=''*len(matriz))
                if l == c:
                    print(f'[{matriz[l][c]:^5}]', end='')

            print()

    elif opcao == 3:
        os.system("cls")
        for l in range(4):
            for c in range(4):
                print(''*4)
                if c > l:
                    print(f'[{matriz[l][c]:^5}]', end='')

            print()

    elif opcao == 4:
        os.system("cls")
        for l in range(4):
            for c in range(4):
                if l > c:
                    print(end=' ')
                    print(f'[{matriz[l][c]:^5}]', end='')

            print()

    elif opcao == 5:
        os.system("cls")
        break

    else:
        os.system("cls")
        raise ValueError('Essa opção não existe')
