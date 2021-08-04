# Funcion para detectar si un numero en cuestion es primo o no
def es_primo(num):
    # Evaluamos cada divisor hasta el mismo numero
    for n in range(2, num):
        # Si hallamos un divisor, devolvemos "false" al no ser un numero primo
        if num % n == 0:
            return False
    # Si no se hallan divisores, es considerado numero primo y se devuelve "true"
    return True

# Funcion para generar arrays de numeros primos hasta limite establecido


def generar_primos(num):
    # Creamos el array
    array_primos = []
    # Recorremos los numeros desde el 2 por definicion de numeros primos,
    # hasta el limite establecido, para hallar los primos antecesores
    for i in range(2, num):
        # Evaluamos con la funcion "es_primo"
        if es_primo(i):
            # Si es primo se agrega al array
            array_primos.append(i)
    return array_primos


# Ejecucion de la funcion
try:
    num = int(input("Ingrese el limite maximo:\n"))
    array_primos = generar_primos(num)
    if array_primos:
        print("Los numeros primos anterior a " +
              str(num) + " son: " + str(array_primos))
    else:
        print("No se hallaron primos anteriores al numero "+str(num))
except:
    print("Valor invalido, debe introducir un numero entero")
