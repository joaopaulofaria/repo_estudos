cars = ['subaru', 'audi', 'honda', 'gm', 'opel']

if 'lancer' not in cars:
    print (cars[3].title() + " Nao esta na lista")
else:
    print (cars[-2].upper() + " Esta na lista")

car = 'Subaru'

print ("Car == subaru, True")
print (car == "subaru")
print ("Car != audi, True")
print (car != "audi")
print ("Car == honda, False")
print (car == "honda")


if car != 'Subaru':
    car = car.upper()
    print (car)
else:
    car = car.lower()
    print (car)

convite = "nao"
idade = 17

if idade >= 18 and convite == "sim":
    print ("Voce esta dentro")
else:
    print ("Volte quando for maior de idade")

if idade >= 18 or convite == "sim":
    print ("Voce esta dentro")
else:
    print ("Volte quando for maior de idade")

print ("s" in car)

age = 12
if age < 4:
    print ("Não paga")
elif age < 18:
    print ("5 reais")
else:
    print ("10 reais")

    