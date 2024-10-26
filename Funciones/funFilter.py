#Función Filter

# def numero_par(num):

#     if num % 2 == 0:

#         return True
    

# numeros=[17,24,15,78,22,49,12]

# print(list(filter(numero_par, numeros)))


#Inclusión de expresión lambda.

# def numero_par(num):

#     if num%2==0:
#         return True

    
# numeros=[17,24,15,78,22,49,12]

# print(list(filter(lambda numero_par: numero_par%2==0, numeros)))


#----------------SEGUNDO EJEMPLO------------

class Empleado:

    def __init__(self, nombre, cargo, salario):
        
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):

        return "{} que trabaja como {} tiene un salario de {} $ " .format(self.nombre, self.cargo, self.salario)
    

listaEmpleados=[

Empleado("Juan", "Director", 750000),
Empleado("Ana", "Presidenta", 850000),
Empleado("Antonio", "Administrativo", 250000),
Empleado("Sara", "Secretaria", 270000),
Empleado("Mario", "Botones", 21000)
]

salariosAltos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salariosAltos:

    print(empleado_salario)

