#Ejemplos de expresiones lambda para simplificar sintaxis


"""def area_triaungulo(base,altura):

    return (base*altura)/2


triangulo1=area_triaungulo(5,7)

triangulo2=area_triaungulo(9,6)

print(triangulo1)
print(triangulo2)"""

#Función Lambda
area_triangulo=lambda base,altura:(base*altura)/2

print(area_triangulo(7,8))


#al_cubo=lambda numero:pow(numero,3)

al_cubo=lambda numero:numero**3

print(al_cubo(13))


destacar_valor = lambda comision:"¡{}! $" .format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))

