import webbrowser
import asyncio
import aiohttp
import bs4
import requests


def new_url(url: list) -> str:
    if len(url) > 1:
        for c in range(len(url)-1):
            url[c] = url[c] + '%20'

    url = ''.join(url)
    url = 'https://pt.wikipedia.org/wiki/' + url.title()

    return url


async def search(url: str):
    return webbrowser.open(url)


def pegar_conteudo(link: str) -> str:
    rq = requests.get(link).text
    soup = bs4.BeautifulSoup(rq, "html.parser")
    result = soup.find("div", {"class": "mw-parser-output"})

    texto = bs4.BeautifulSoup(result.decode(), "html.parser").find_all("p")[0]

    return texto.text


if __name__ == '__main__':
    url = input('Digite o que você quer pesquisar: ').split()

    # t1 = asyncio.run(search(fuc_url))
    result = pegar_conteudo(new_url(url))

    print(f'\nResumo: {result}')
