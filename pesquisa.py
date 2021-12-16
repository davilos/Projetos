import webbrowser

url = input('Digite o que você quer pesquisar: ')

url = url.split()

if len(url) > 1:
    for c in range(len(url)-1):
        url[c] = url[c] + '%20'

print(url)

url = ''.join(url)

url = 'https://www.google.com.br/search?q=' + url

webbrowser.open(url)
