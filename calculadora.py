from typing import Union

print('Calculadora')

number = Union[int, float]


def calculator(n1: number, n2: number, opc: number, aux: number = 0, /) -> number:
    switch = {
        '+': n1 + n2,
        '*': n1 * n2,
        '/': n1 / n2,
        '-': n1 - n2,
        '**': n1 ** n2,
        '%': n1 * n2 / 100
    }
    return switch.get(opc, aux)


try:
    num: list = input('Digite os dois números: ').split()
    op: str = input('Digite a operação: ').upper()

    if '.' in num[0] and '.' in num[1]:
        print(aux := calculator(float(num[0]), float(num[2]), op))
        
        while True:
            op: str = input('Digite a operação: ').upper()
            if op != 'AC':
                num: str = input('Digite o número: ')
                if '.' in num:
                    print(aux := calculator(aux, float(num), op, aux))
                else:
                    print(aux := calculator(aux, int(num), op, aux))
            else:
                break

    elif '.' in num[0]:
        print(aux := calculator(float(num[0]), int(num[1]), op))

        while True:
            op: str = input('Digite a operação: ').upper()
            if op != 'AC':
                num: str = input('Digite o número: ')
                if '.' in num:
                    print(aux := calculator(aux, float(num), op, aux))
                else:
                    print(aux := calculator(aux, int(num), op, aux))
            else:
                break

    elif '.' in num[1]:
        print(aux := calculator(float(int[0]), float(num[1]), op))

        while True:
            op: str = input('Digite a operação: ').upper()
            if op != 'AC':
                num: str = input('Digite o número: ')
                if '.' in num:
                    print(aux := calculator(aux, float(num), op, aux))
                else:
                    print(aux := calculator(aux, int(num), op, aux))
            else:
                break

    else:
        print(aux := calculator(int(num[0]), int(num[1]), op))

        while True:
            op: str = input('Digite a operação: ').upper()
            if op != 'AC':
                num: str = input('Digite o número: ')
                if '.' in num:
                    print(aux := calculator(aux, float(num), op, aux))
                else:
                    print(aux := calculator(aux, int(num), op, aux))
            else:
                break

except (TypeError, ValueError, IndexError) as erro:
    print(f'\033[31mHouve um erro: {erro}\033[m')

print('\033[1;97mPrograma finalizado!\033[m')
