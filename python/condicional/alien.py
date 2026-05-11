#alien_color = ['green', 'yellow', 'red']

alien_color = 'red'
if alien_color == 'green':
    ponto = 5
    print (str(ponto) + " pontos")
elif alien_color == 'red':
    ponto = 7
    print (str(ponto) + " pontos")
elif alien_color == 'yellow':
    ponto = 10
    print (str(ponto) + " pontos")

age = 100
if age <= 2:
    print ("bebe")
elif age <= 4:
    print ("garoto")
elif age <= 13:
    print ("adolescente")
elif age <= 20:
    print ("adulto")
elif age >= 65:
    print ("idoso")