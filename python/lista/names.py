names = ['joao', 'bruno', 'mateus']

print (names[0])
print (names[1])
print (names[-1])

message_full = "Ola " + names[0] + ", estamos te esperando"

print (message_full)

sonho = ['casa', 'carro', 'trabalho', 'dinheiro']
message_full
print ("Gostaria de ter: " + sonho[0])
print ("Gostaria de ter: " + sonho [-3])
print ("Gostaria de ter: "+ sonho [-1])

sonho [0] = "viagem"

print (sonho)

sonho.append('casa')
print (sonho)

motos = []
motos.append('honda')
motos.append('suzuki')
print(motos)

motos.insert(1, 'ducati')
print (motos)

del motos[0]
print (motos)

print (motos[1])
motos[0] = 'yamaha'

print (motos)

sonho_pop = sonho.pop(1)
print (sonho)
print (sonho_pop)

print (sonho)

longe_dificil = "viagem"
sonho.remove(longe_dificil)
print (sonho)
