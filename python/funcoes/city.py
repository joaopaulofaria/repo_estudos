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