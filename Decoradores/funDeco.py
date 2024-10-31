#Las funciones decoradores añaden funcionalidades a otras funciones.

def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        #Acciones adicionales que decora

        print("Vamos a realizar un cálculo: ")

        funcion_parametro()

        print("Hemos terminado el cálculo")

    return funcion_interior




@funcion_decoradora
def suma():

    print(15+20)




def resta():

    print(30-10)


suma()