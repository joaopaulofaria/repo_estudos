ingredientes = ['cebola', 'calabresa']
if ingredientes:
    for ingrediente in ingredientes:
        print (".")
else:
    print ("Esta vazio")

pedidos = ['tomate', 'cebola']

for pedido in pedidos :
    if pedido in ingredientes:
        print ("Adicionando")
    else:
        print ("não temos esse ingrediente")