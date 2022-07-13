from typing import Union

print('Calculadora')

number = Union[int, float]


def calculator(n1: number, n2: number, opc: str, aux: number = 0, /) -> number:
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
    num_list: list = input('Digite os dois números: ').split()
    op_1: str = input('Digite a operação: ').upper()

    if '.' in num_list[0] and '.' in num_list[1]:
        print(aux := calculator(float(num_list[0]), float(num_list[1]), op_1))

        while (op_2 := input('Digite a operação: ').upper()) != 'AC':
            num_1: str = input('Digite o número: ')
            if '.' in num_1:
                print(aux := calculator(aux, float(num_1), op_2, aux))
            else:
                print(aux := calculator(aux, int(num_1), op_2, aux))

    elif '.' in num_list[0]:
        print(aux := calculator(float(num_list[0]), int(num_list[1]), op_1))

        while (op_3 := input('Digite a operação: ').upper()) != 'AC':
            num_2: str = input('Digite o número: ')
            if '.' in num_2:
                print(aux := calculator(aux, float(num_2), op_3, aux))
            else:
                print(aux := calculator(aux, int(num_2), op_3, aux))

    elif '.' in num_list[1]:
        print(aux := calculator(int(num_list[0]), float(num_list[1]), op_1))

        while (op_4 := input('Digite a operação: ').upper()) != 'AC':
            num_3: str = input('Digite o número: ')
            if '.' in num_3:
                print(aux := calculator(aux, float(num_3), op_4, aux))
            else:
                print(aux := calculator(aux, int(num_3), op_4, aux))

    else:
        print(aux := calculator(int(num_list[0]), int(num_list[1]), op_1))

        while (op_5 := input('Digite a operação: ').upper()) != 'AC':
            num_4: str = input('Digite o número: ')
            if '.' in num_4:
                print(aux := calculator(aux, float(num_4), op_5, aux))
            else:
                print(aux := calculator(aux, int(num_4), op_5, aux))

except (TypeError, ValueError, IndexError) as erro:
    print(f'\033[31mHouve um erro: {erro}\033[m')

print('\033[1;97mPrograma finalizado!\033[m')
