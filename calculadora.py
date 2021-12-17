print('Calculadora')


def soma(n1, n2):
    return n1 + n2


def mult(n1, n2):
    return n1 * n2


def divi(n1, n2):
    return n1 / n2


def sub(n1, n2):
    return n1 - n2


def pot(n1, n2):
    return n1 ** n2


def fat(n1):
    f = 1
    for n in range(n1, 0, -1):
        f *= n

    return f


while True:
    num1 = int(input('Digite um número: '))
    op = input('Digite sua opção: ')
    num2 = int(input('Digite outro número: '))

    if op == '+':
        print(soma(num1, num2))
        aux = soma(num1, num2)
        while op != 'AC':
            num = int(input('Digite um número: '))
            op = input('Digite sua opção: ').upper()

            if op == '+':
                print(soma(aux, num))
                aux = soma(aux, num)
            elif op == '*':
                print(mult(aux, num))
                aux = mult(aux, num)
            elif op == '/':
                print(divi(aux, num))
                aux = divi(aux, num)
            elif op == '-':
                print(sub(aux, num))
                aux = sub(aux, num)
            elif op == '**':
                print(pot(aux, num))
                aux = pot(aux, num)

    elif op == '*':
        print(mult(num1, num2))
        aux = mult(num1, num2)
        while op != 'AC':
            num = int(input('Digite um número: '))
            op = input('Digite sua opção: ').upper()

            if op == '+':
                print(soma(aux, num))
                aux = soma(aux, num)
            elif op == '*':
                print(mult(aux, num))
                aux = mult(aux, num)
            elif op == '/':
                print(divi(aux, num))
                aux = divi(aux, num)
            elif op == '-':
                print(sub(aux, num))
                aux = sub(aux, num)
            elif op == '**':
                print(pot(aux, num))
                aux = pot(aux, num)
    elif op == '/':
        print(divi(num1, num2))
        aux = divi(num1, num2)
        while op != 'AC':
            num = int(input('Digite um número: '))
            op = input('Digite sua opção: ').upper()

            if op == '+':
                print(soma(aux, num))
                aux = soma(aux, num)
            elif op == '*':
                print(mult(aux, num))
                aux = mult(aux, num)
            elif op == '/':
                print(divi(aux, num))
                aux = divi(aux, num)
            elif op == '-':
                print(sub(aux, num))
                aux = sub(aux, num)
            elif op == '**':
                print(pot(aux, num))
                aux = pot(aux, num)
    elif op == '-':
        print(sub(num1, num2))
        aux = sub(num1, num2)
        while op != 'AC':
            num = int(input('Digite um número: '))
            op = input('Digite sua opção: ').upper()

            if op == '+':
                print(soma(aux, num))
                aux = soma(aux, num)
            elif op == '*':
                print(mult(aux, num))
                aux = mult(aux, num)
            elif op == '/':
                print(divi(aux, num))
                aux = divi(aux, num)
            elif op == '-':
                print(sub(aux, num))
                aux = sub(aux, num)
            elif op == '**':
                print(pot(aux, num))
                aux = pot(aux, num)
    elif op == '**':
        print(pot(num1, num2))
        aux = pot(num1, num2)
        while op != 'AC':
            num = int(input('Digite um número: '))
            op = input('Digite sua opção: ').upper()

            if op == '+':
                print(soma(aux, num))
                aux = soma(aux, num)
            elif op == '*':
                print(mult(aux, num))
                aux = mult(aux, num)
            elif op == '/':
                print(divi(aux, num))
                aux = divi(aux, num)
            elif op == '-':
                print(sub(aux, num))
                aux = sub(aux, num)
            elif op == '**':
                print(pot(aux, num))
                aux = pot(aux, num)
