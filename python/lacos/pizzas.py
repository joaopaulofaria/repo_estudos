pizzas = ['calabresa', 'frango', 'moda']

for pizza in pizzas:
    print ("Gosto de pizza de " + pizza.title())

print ("Eu realmente adoro pizza de " + pizza)

amigo_pizza = pizzas[:]
pizzas.append('palmito')
amigo_pizza.insert(3,'napolitana')

print (pizzas)
print (amigo_pizza)


print ("Minhas pizzas favoritas sao: ")
for pizza in pizzas:
    print (pizza)

print ("As pizzas favoritas do meu brodi sao: ")
for amigo in amigo_pizza:
    print (amigo)


#animais = ['dog', 'cat', 'fish']

#for animal in animais:
   # print (" O " + animal.title() + " seria um otimo animal")
   # print (animal)
#print ("Qualquer uma desses animais seria de estimação")

print (pizza)