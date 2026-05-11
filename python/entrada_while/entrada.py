#message = input("Diga algo: ")
#print (message)

#prompt = "personalizar mensagem para usuario"
#prompt += "\nqual seu primeiro nome? "
#print (prompt)

#age = input ("sua idade? ")
#print (int(age) >= 18)

numbers = []
limite = int(input ("Defina um numero limite: "))

for number in range(limite):
    number = input ("Digite " + str(limite) + " numeros : ") 
    numbers.append(number)
print (numbers)

for number in numbers:
    if int(number) % 2 == 0:
        print (number + " é par")
    else:
        print (number +  " é impar")

        