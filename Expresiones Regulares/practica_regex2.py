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


#Busqueda

lista_dominios=["http://informaticaemespaña.es",
                "https://pildorasinformaticas.es",
                "https://pildorasinformaticas.es"]

for elemento in lista_dominios:

    if re.findall('[ñ]', elemento):

        print(elemento)


#tercer ejemplo

lista_nombres2=['hombres',
                'mujeres',
                'mascoa',
                'niños',
                'niñas']

for elemento in lista_nombres2:
    if re.findall('niñ[oa]s', elemento):

        print(elemento)

#cuarto ejemplo

lista_nombres3=['camion',
                'camión',
                'automovil',
                'motocicleta']

for elemento in lista_nombres3:
    if re.findall('cami[oó]n', elemento):
        print(elemento)