import re

lista_nombres=['Ana Gómez',
               'María Martín',
               'Sandra López',
               'Santiago Martín',
               'Sandra Fernandez']


for elemento in lista_nombres:

    if re.findall('^Sandra', elemento):

        print(elemento)


for elemento in lista_nombres:

    if re.findall('Martín$', elemento):

        print(elemento)