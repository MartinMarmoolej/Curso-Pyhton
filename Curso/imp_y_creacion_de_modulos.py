########################Importar modulos##############################
import math


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

"""
En este ejemplo, se importa el módulo math utilizando la declaración 
import. Luego, se utiliza la función sqrt() del módulo math para 
calcular la raíz cuadrada de 25.
"""

from math import sqrt 
#mismo resultado pero solo utilizando la funcion
resultado = sqrt(25)
print(resultado)  # Imprime 5.0
"""
En este caso, se importa solo la función sqrt() del módulo math,
lo que nos permite utilizarla directamente sin tener que precederla 
con el nombre del módulo.
"""

#Funciones y clases de modulos estandar
#Math, Random, Datetime
import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual

#######################Creacion de modulos propios#####################

#Creacion y utilizar modulos personalizados
import mi_modulo

mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"

resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

#importacion de nuestros modulos operaciones y utilidades
import operaciones
import utilidades

resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")

############################Paquetes#####################################
#Crear y utilizar paquetes
from mi_paquete import modulo1, modulo2

modulo1.funcion1()
modulo2.funcion2()