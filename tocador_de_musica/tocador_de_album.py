import pygame
import random
import listas_tocador

print(sorted(listas_tocador.albuns, key=lambda a: a["Ano"], reverse=True))

print('-=-' * 50)

select_album = input('Escolha o álbum: ').strip().title()

# Realiza a pesquisa do álbum na lista "albuns", pra depois imprimir o ano do álbum.
ano_do_album = filter(lambda album: select_album.lower() in album.get("Nome").lower(), listas_tocador.albuns)

# Realiza a pesquisa do álbum na lista "musicas".
musicas_do_album = filter(lambda album: select_album.lower() in album.get("Nome").lower(), listas_tocador.musicas)

# Desempacota somente as músicas da variável "x".
musics = [[v for k, v in m.items() if k == 'Músicas'] for m in musicas_do_album]

print(f'\033[1;97m{select_album}\033[m')
print('\033[1;97mArctic Monkeys\033[m')
print(f'Álbum ° {list(y["Ano"] for y in ano_do_album)}')

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
