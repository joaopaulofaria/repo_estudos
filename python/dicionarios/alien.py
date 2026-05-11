alien_0 = {'color': 'green', 'points': 5}
print (alien_0['color'])
print (alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print (alien_0['x_position'])

alien_1 = {}
alien_1['color'] = 'green'
print (alien_1)

alien_1['color'] = 'red'
print (alien_1)

if alien_1['color'] == 'green':
    alien_1['x_position'] = 1
elif alien_1['color'] == 'red':
    alien_1['x_position'] = 10

print (alien_1)

del alien_1['x_position']

print (alien_1)

favorite_languages = {
    'edu': 'python',
    'joao': 'rust',
    'luiz': 'java'
}

print ('linguagem favorita: ' + 
        favorite_languages['joao'])


#for name, language in favorite_languages.items():
#    print (name.upper() + " gosta de " + language.title())

for name in favorite_languages.keys():
    print (name.title())


friends = ['joao', 'luiz']
for name in favorite_languages.keys():
    if name in friends:
        print ("Opa " + name.title())

for name in sorted(favorite_languages.keys()):
    print (name)

for name in set(favorite_languages.values()):
    print (name)

aliens = [alien_0, alien_1]
for alien in aliens:
    print (alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'nivel': '5'}
    aliens.append (new_alien)

for alien in aliens [:5]:
    print (alien)

print (str(len(aliens)))

aliens = []
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': '5'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'red'

for alien in aliens [0:5]:
    print (alien)



pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], }
for topping in pizza ['toppings']:
    print (topping)

