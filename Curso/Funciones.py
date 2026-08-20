#Definicion y llamado de funciones

def saludo():
    print("¡Hola, mundo!")

saludo()  # Imprime "¡Hola, mundo!

#Parametros y argumentos

def saludo2(nombre):
    print(f"¡Hola, {nombre}!")

saludo2("Juan")  # Imprime "¡Hola, Juan!"
saludo2("María")  # Imprime "¡Hola, María!"

#Valores de retorno
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Imprime 7

#Funciones anonimas (lambda)
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25

#Variables (locales y globales)

def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función

variable_global = 20

def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar

funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
#print(variable_local)  # Genera un error, la variable no está definida en este alcance.

#EJERCICIOS
def calcular_media(*numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    return media

print("Media", calcular_media(10, 20, 30, 40))

#######################################

def sumar_3(x):
    return x + 3

sumar = lambda x:x + 3

print("Sumarle 3 a un numero:", sumar(5))

#Documentacion de funciones (docstrings)
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return base * altura 
print(area_rectangulo(2.33, 7.5))

#Funciones con numero variable de argumentos
#Python permite definir funciones que acepten un número variable de argumentos. Esto se logra utilizando el operador * antes del nombre del parámetro.
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22