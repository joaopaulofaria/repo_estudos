#or number in range (1,21):
#    print(number)

numbers = [number for number in range (1,21,2)]
print (numbers)



#print (min(numbers))
#print (max(numbers))
#print (sum(numbers))

multiplos = [x for x in range (3, 31,3)]
print (multiplos)

cubos = [x ** 3 for x in range (1,11)]
print (cubos)

for cubo in cubos:
    print (cubo)

for cubo in range (1,11):
    print (cubo ** 3)