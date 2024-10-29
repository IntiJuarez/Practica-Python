import re


lista_nombres=['Ana',
               'Pedro',
               'María',
               'Rosa',
               'Sandra',
               'Celia']


for elemento in lista_nombres:
    
    if re.findall('[o-t]', elemento):

        print(elemento)


#otra forma de buscar por rango

lista_nombres2=['Ma1',
                'Se1',
                'Ma2',
                'Ba1',
                'Ma3',
                'Va2',
                'Va1'
                'Ma4']

for elemento in lista_nombres2:

    if re.findall('Ma[0-3]', elemento):

        print(elemento)