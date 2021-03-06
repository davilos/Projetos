from passlib.hash import pbkdf2_sha256 as cryp
from csv import writer, reader
import os


# Desenvolvedor
class Cadastro:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def __str__(self):
        return 'Essa é uma classe do tipo Cadastro'

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    def user(self):
        return self.__email.split('@')[0]


class User(Cadastro):
    count = 0

    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        self.__num = User.count + 1
        User.count = self.__num

    def __str__(self):
        return 'Essa é uma classe do tipo User'

    @classmethod
    def contador(cls):
        return f'Temos {cls.count} usuário(s) no sistema.'


def make_user(user_class: type[User], nome: str, email: str, senha: str) -> User:
    return user_class(nome=nome, email=email, senha=senha)


with open('usuarios.csv', 'a+', encoding='utf8', newline='') as arq:
    esc_csv = writer(arq)
    if os.path.exists('usuarios.csv'):
        pass
    else:
        esc_csv.writerow(["Nome", "Email", "Senha"])
    opcao = None
    while opcao != 'sair':
        opcao = input('Digite sair caso queira parar: ').lower()
        if opcao == 'sair':
            break
        else:
            print(f'\033[1;97mCADASTRO\033[m')
            nome_cadastro = input('Digite o nome: ')

            if nome_cadastro != '':
                email_cadastro = input('Digite o e-mail: ')

                if '@' and '.com' in email_cadastro:
                    senha_cadastro = input('Digite a senha: ')

                    if len(senha_cadastro) >= 8:
                        user = make_user(nome_cadastro, email_cadastro, senha_cadastro)
                        with open('usuarios.csv') as arq2:
                            lei_csv = reader(arq2)
                            for n in lei_csv:
                                verificador = 0
                                if user.nome.title() == n[0] or user.email.title() == n[1]:
                                    verificador += 1
                                    print('Usuário ou e-mail já cadastrados!')
                                    break
                            if verificador == 0:
                                esc_csv.writerow([user.nome, user.email, user.senha])
                    else:
                        print('\033[31mDigite uma senha mais forte!\033[m')
                else:
                    print('\033[31mDigite um e-mail válido!\033[m')
            else:
                print('\033[31mNome indisponível!\033[m')

# Usuário
option = input('Digite o nome de usuário ou senha: ')
password = input('Digite a senha: ')

if '@' and '.com' in option:
    with open('usuarios.csv') as arq:
        lei_csv = reader(arq)
        verificador = 0
        for n in lei_csv:
            if option == n[1] and cryp.verify(password, n[2]):
                verificador += 1
                print(f'Seja bem-vindo {n[0]}')
            else:
                pass
        if verificador == 0:
            print('\033[31mE-mail ou senha incorretos\033[m')

else:
    with open('usuarios.csv') as arq:
        lei_csv = reader(arq)
        verificador = 0
        for n in lei_csv:
            if option.title() == n[0] and cryp.verify(password, n[2]):
                verificador += 1
                print(f'Seja bem-vindo {n[0]}')
            else:
                pass
        if verificador == 0:
            print('\033[31mUsuário ou senha incorretos\033[m')
