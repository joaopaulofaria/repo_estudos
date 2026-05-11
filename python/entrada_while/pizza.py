message_0 = ("Digite os ingredientes: ")
active = True
ingredientes = []

while active:
    message = input (message_0)
    if message != 'quit':
        ingredientes.append(message)
        message = "Adicionando " + message
        print (message)
        print (ingredientes)
    else:
        active = False

#while True:
 #   idade = int(input ("Qual a sua idade: "))
 #   print ("Digite 0 para sair")
#
 #   if idade == 0:
 #       break
#
#    if idade < 3:
#        print ("Ingresso gratuito")
#    elif idade >= 3 and idade <= 12:
#        print ("10 reais")
#    elif idade > 12:
#        print ("15 reais")

#active = True
#while active == True:
#    idade = int(input ("Qual a sua idade: "))
#    print ("Digite 0 para sair")
#
#    if idade == 0:
#        active = False
#
#    if idade < 3:
#        print ("Ingresso gratuito")
#    elif idade >= 3 and idade <= 12:
#        print ("10 reais")
#    elif idade > 12:
#        print ("15 reais")

idade = int(input ("Digite a sua idade (0 para sair)"))
while idade != 0:

    if idade < 3:
        print ("Ingresso gratuito")
    elif idade >= 3 and idade <= 12:
        print ("10 reais")
    elif idade > 12:
        print ("15 reais")
    
    idade = int(input ("Digite a sua idade (0 para sair)"))

