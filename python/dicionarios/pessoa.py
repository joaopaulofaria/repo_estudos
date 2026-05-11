people = {'cor': 'branca', 'altura': 175, 'peso': 76, 'primeiro_nome': "joao paulo", 'idade': 21}

for valor in people:
    print (people[valor])

pessoas = {}
pessoas = {
    'joao': 0,
    'luiz': 2,
    'julia': 10
}

print (pessoas)

for pessoa in pessoas:
    print (pessoa + " = " + str(pessoas[pessoa]))

palavras = {'palavra1': 'concatenar', 'palavra2': 'bitwise'}

for palavra in palavras:
    print (palavra + " = " + palavras[palavra] + "\n")

user_0 = {'username': 'joaofaria', 'first': 'joao', 'last': 'faria'}

for key, value in user_0.items():
    print ("\nKey: " + key)
    print ("Value: " + value)

favorite_language = {'jen': ['python', 'c'], 'sarah': ['c', 'haskell']}
for name, languages in favorite_language.items():
    print (name)
    for language in languages:
        print (language)

users = {'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'german', }}

for username, user_info in users.items():
    print ("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print ("\tFull name: " + full_name.title()) 
    print("\tLocation: " + location.title())