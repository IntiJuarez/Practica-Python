#Las funciones decoradores añaden funcionalidades a otras funciones.

#*args(args es una convención) = permite recibir un número indeterminado de parámetros
#Pasar parámetros con doble valor (keywords arguments) con doble ** 

def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        #Acciones adicionales que decora

        print("Vamos a realizar un cálculo: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora
def potencia(base, exponente):

    print(pow(base,exponente))



@funcion_decoradora
def suma(num1, num2, num3):

    print(num1 + num2 + num3)



@funcion_decoradora
def resta(num1, num2, num3):

    print(num1 - num2 - num3)


suma(10,10,10)

resta(40,20,10)

potencia(base=5,exponente=3)