def areaTriangulo(base,altura):

    """
    Calcula el área de un triángulo dado    

    >>> areaTriangulo(3,6)
    'El área del triáungulo es: 9.0'

    """

    return "El área del triáungulo es: " + str((base*altura)/2)


#print(areaTriangulo(2,4))

#realizar pruebas
import doctest

doctest.testmod()


