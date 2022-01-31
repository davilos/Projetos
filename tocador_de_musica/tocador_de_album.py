import pygame
import random
import listas_tocador

# Recebe os álbuns e ordena eles pela key "Ano".
albuns_ordenados = sorted(listas_tocador.albuns, key=lambda album: album["Ano"], reverse=True)

for x in range(len(albuns_ordenados)):
    print(f'\033[1;97m{albuns_ordenados[x]["Nome"]} º {albuns_ordenados[x]["Ano"]}\033[m')

print('-=-' * 45)

select_album = input('Escolha o álbum: ').strip().title()

print('-=-' * 45)

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
            listas_tocador.albuns)
    )
)

# Realiza a pesquisa do álbum na lista "musicas".
musicas_do_album = filter(lambda album: select_album.lower() in album.get("Nome").lower(), listas_tocador.musicas)

# Desempacota somente as músicas da variável "musicas_do_album".
musics = [[v for k, v in m.items() if k == 'Músicas'] for m in musicas_do_album]

print(f'\033[1;97m{select_album}\033[m')
print('\033[1;97mArctic Monkeys\033[m')
print(f'Álbum ° {ano_do_album[0]}')  # ano_do_album[0]["Ano"]

options = int(input('[1] Ordenado [2] Aleatório: '))

if options == 1:
    for m in range(len(musics[0][0])):
        print(musics[0][0][m])
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(f'{musics[0][0][m]}.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

else:
    random_list = []
    while len(random_list) < 13:
        for m in range(len(musics[0][0])):
            random_list.append(random.choice(musics[0][0]))

            for x in random_list:
                while random_list.count(x) > 1:
                    random_list.remove(x)
    for m in random_list:
        print(m)
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(f'{m}.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
