class Areas:

    """Esta clase calcula las áreas de diferentes figuras geométricas"""

    def areaCaudrado(lado):

        """Calcula el área de un cuadrado
        elevando al cuadrado el lado pasado por parámetro"""
    
        return " EL área de un cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):

        """Calcula el área de un triángulo utilizando
        los parámetros base y altura"""

        return " El área de un triáungulo es: " + str((base*altura)/2)


print(Areas.areaTriangulo(2,7))
print(Areas.areaCaudrado(5))

#imprime documentación asociada a la función
#print(areaCaudrado.__doc__)

#otra forma de impresión
#help(areaCaudrado)
#help(areaTriangulo)

#En caso de claase:
#help(Areas.areaCaudrado)
help(Areas)