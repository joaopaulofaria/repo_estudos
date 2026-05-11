#def greet_user():
#    """"Exibe uma saudacao"""
#    print ("Hello")

#greet_user()

#def greet_user(username):
#    """"Exibe uma saudacao"""
#    print ("Hello, " + username)

#greet_user('jesse')

def disply_message():
    """Aprendizado do capitulo"""
    print ("Estudando funcoes")

disply_message()

def favorite_book(title):
    print ("Meu livro favorito é: " + title)

favorite_book('alice no pais das maravilhas')

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre animal de estimacao"""
    print (animal_type)
    print (pet_name.upper())

#argumentos posicionais
describe_pet('rato', 'harry')
describe_pet('cat', 'benson')

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre animal de estimacao"""
    print (animal_type)
    print (pet_name.upper())

#Argumento nomeado
describe_pet(animal_type='dog', pet_name='max')

def describe_pet(pet_name, animal_type='lion'):
    """Exibe informações sobre animal de estimacao"""
    print (animal_type)
    print (pet_name.upper())

#Argumento posicial e default
describe_pet(pet_name='duran')

def make_shirt(lenght, message = 'Seu tamanho é'):
        print (message)
        print (lenght)

make_shirt('M', 'Seu tamanho é')
make_shirt(lenght='M')

def formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = formatted_name('jimi', 'hendrix')
print (musician)

def build_person(first_name, last_name, age=""):
    person = {'first': first_name, 'last': last_name}
    if age:
         person ['age'] = age
    return person

musician = build_person ('jimi', 'hendrix', age=27)
print (musician)


def formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("(enter 'q' at any time to quit)")
    print ("Diga seu nome: ")

    f_name = input("NOME ")
    if f_name == 'q': 
        break
    
    l_name = input ("Last name: ")
    if l_name == 'q': 
        break
    
    formatted_name1 = formatted_name(f_name, l_name) 
    print("\nHello, " + formatted_name + "!")