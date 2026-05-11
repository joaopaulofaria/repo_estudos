cars = ['bmw', 'audi', 'mercedes', 'honda']

for car in cars:
    if car == 'bmw':
        print (car.upper())
    else:
        print (car.title())


for car in cars:
    car.lower()
    print (car)

pizza = "calabresa"

if pizza != "portuguesa":
    print ("Não quero cebola")


age = 18

if age <= 18:
    print ("Menor de idade")
else:
    print ("Maior de idade")

ingredientes = ('cebola', 'tomate', 'pimenta')
'pimenta' in ingredientes

ingrediente = "cebola"
if ingrediente not in ingredientes:
    print ("Essa pizza não tem " + ingrediente.title())

    