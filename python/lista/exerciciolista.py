convidados = ['irmao', 'pai', 'mae']

message = convidados[-1] + ", Voce gostaria de jantar?"
print (message)

print (convidados[-1])
convidados[-1] = "namorada"

print (convidados)

convidados.insert(0, 'amigo')
convidados.insert(-2, 'avó')
convidados.append('amigo_2')

print (convidados)

print ("Vou reduzir a lista de convidados para 2 pessoas:")
convidado1 = convidados.pop()
print ("Sinto muito por nao ter te chamado:" + convidado1)
convidado1 = convidados.pop(0)
print ("Voce foi removido da lista: " + convidado1)

convidados.remove('avó')
convidados.remove('pai')

print (convidados)

del convidados [-1]
del convidados [0]

print (convidados)
