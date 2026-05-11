naoconfirmados_users = ['alice', 'brain', 'candace']
confirmados_users = []

while naoconfirmados_users:
    atual_user = naoconfirmados_users.pop()
    print (atual_user)
    confirmados_users.append(atual_user)
    
print ("\nUsuarios confirmados: ")
for confirmado_user in confirmados_users:
    print (confirmado_user)

print (confirmados_users)

responses = {}
active = True

while active:
    name = input ("Qual seu nome? ")
    response = input ("Qual seu esporte favorito? ")
    responses[name] = response
    repeat = input ("Mais alguem vai responder? ")
    if repeat == 'no':
        active = False

for name, response in responses.items():
    print (name + " gosta de " + response)