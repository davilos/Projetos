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
        r = soma(num1, num2)
        while op != 'AC':
            n = int(input('Digite um número: '))
            op = input('Digite sua opção: ').upper()

            if op == '+':
                print(soma(r, n))
                r = soma(r, n)
            elif op == '*':
                print(mult(r, n))
                r = mult(r, n)
            elif op == '/':
                print(divi(r, n))
                r = divi(r, n)
            elif op == '-':
                print(sub(r, n))
                r = sub(r, n)
            elif op == '**':
                print(pot(r, n))
                r = pot(r, n)

    elif op == '*':
        print(mult(num1, num2))
    elif op == '/':
        print(divi(num1, num2))
    elif op == '-':
        print(sub(num1, num2))
    elif op == '**':
        print(pot(num1, num2))


