from matematica import suma
from matematica import resta
from matematica import potencia
from matematica import division

if __name__ == "__main__":
    # funcion de redefinicion con parámetros
    def smart_div(func):
        def inner(a, b):
            if b == 0:
                b = 1
            return func(a, b)
        return inner

    # call funcion de redefinicion, argumento funcion original
    div = smart_div(division)

    suma = suma(2,3)
    resta = resta(2,3)
    potencia = potencia(2,2)
    division = div(3,0)

    print ("contexto:", __name__)
    print ("Potencia: ",potencia)
    print ("Suma:", suma)
    print ("Resto:", resta)
    print ("Division:",division)
