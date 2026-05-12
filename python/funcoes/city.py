def city_country(city, country = 'chile'):
     print (city, country)

city_country('santiago', 'chile')
city_country(city = 'santiago', country= 'chile')
city_country(city = 'santiago')

def make_album(artista_album, titulo_album, faixa_album=''):
     album = {'artista': artista_album, 'titulo': titulo_album, }
     if faixa_album:
          album['faixa'] = faixa_album
     return album

print (make_album ('linkin park', 'meteora'))

def make_album(artista, titulo):
    album = {
        'artista': artista,
        'titulo': titulo
    }
    return album


while True:
    print("\nDigite o nome do artista:")
    print("Digite 'q' para sair.")

    artista = input()

    if artista == 'q':
        break

    print("Digite o título do álbum:")
    titulo = input()

    if titulo == 'q':
        break

    album = make_album(artista, titulo)

    print(album)


