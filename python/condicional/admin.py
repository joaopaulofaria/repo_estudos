names = ['joao', 'luiz','admin', 'pai', 'mae']

if names:
    for name in names:
        if name == 'admin':
            print ("Olá admin, gostaria de ver um relatório de status?")
        else:
            print ("Saudacao a " + name)
else:
    print ("A lista esta vazia")

current_users = ['joao', 'luiz','admin', 'pai', 'mae']
new_users = ['ronilsa', 'JUlia', 'enio', 'Joao', 'luiz', 'miguel']


for new_user in new_users:
    new_users = [new_user.lower() for new_user in new_users]
print (new_users)

for new_user in new_users:
    if new_user in current_users:
        print ("Forneça um novo nome")
    else:
        print ("Nome disponivel")

