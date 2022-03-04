from pygame import (
    mixer,
    init
)
from random import choice
from listas_tocador import *
count = 0

if __name__ == '__main__':

    # Recebe os álbuns e ordena eles pela key "Ano".
    albuns_ordenados = sorted(albuns, key=lambda album: album["Ano"], reverse=True)

    for x in range(len(albuns_ordenados)):
        print(f'\033[1;97m{albuns_ordenados[x]["Nome"]} º {albuns_ordenados[x]["Ano"]}\033[m')

    print('-=-' * 25)
    select_album = input('Escolha o álbum: ').strip().title()
    print('-=-' * 25)

    for alb in albuns:
        if select_album.lower() == alb['Nome'].lower():
            # Realiza a pesquisa do álbum na lista "albuns", pra depois imprimir o ano do álbum.
            """
            ano_do_album = list(
                    filter(
                        lambda album: select_album.lower() in album.get("Nome").lower(),
                        listas_tocador.albuns)
                )
            """
            ano_do_album = list(
                map(
                    lambda album: album["Ano"],
                    filter(
                        lambda album: select_album.lower() in album.get("Nome").lower(),
                        albuns
                    )
                )
            )

            # Realiza a pesquisa do álbum na lista "musicas", pra depois tocar as músicas.
            """
            musicas_do_album = list(
                filter(
                    lambda album: select_album.lower() in album.get("Nome").lower()
                    , listas_tocador.musicas)
            )
            """
            musicas_do_album = list(
                map(
                    lambda album: album["Músicas"],
                    filter(
                        lambda album: select_album.lower() in album.get("Nome").lower(),
                        musicas
                    )
                )
            )

            print(f'\033[1;97m{select_album}\033[m')
            print('\033[1;97mArctic Monkeys\033[m')
            print(f'Álbum ° {ano_do_album[0]}')  # ano_do_album[0]["Ano"]

            try:
                options = int(input('[1] Ordenado [2] Aleatório: '))
            except ValueError as err:
                print(f'Digite um valor inteiro!')
            else:
                if options == 1:
                    for m in range(len(musicas_do_album[0])):
                        print(musicas_do_album[0][m])
                        mixer.init()
                        init()
                        mixer.music.load(f'{musicas_do_album[0][m]}.mp3')
                        mixer.music.play()
                        while mixer.music.get_busy():
                            pass

                elif options == 2:
                    random_list = []
                    while len(random_list) < len(musicas_do_album[0]):
                        for m in range(len(musicas_do_album[0])):
                            random_list.append(choice(musicas_do_album[0]))

                            for x in random_list:
                                while random_list.count(x) > 1:
                                    random_list.remove(x)
                    for m in random_list:
                        print(m)
                        mixer.init()
                        init()
                        mixer.music.load(f'{m}.mp3')
                        mixer.music.play()
                        while mixer.music.get_busy():
                            pass
                else:
                    raise ValueError('Valor inválido!')
        else:
            count += 1
            if count == 7:
                raise ValueError(f'Álbum {select_album} não existe!')
