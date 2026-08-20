# ###############Entrada de datos del usuario################
# """
# Para obtener información del usuario
# durante la ejecución del programa,
# podemos utilizar la función input().
# Esta función muestra un mensaje en la pantalla
# y espera a que el usuario ingrese un valor.
# """
# nombre = input("Ingresa tu nombre: ")
# edad = input("Ingresa tu edad: ")

# print("Hola, " + nombre + "!")
# print("Tienes " + edad + " años.")

# #int o float

# edad = int(input("Ingresa tu edad: "))

# if edad >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("Eres menor de edad.")


# #Salida de datos
# nombre2 = "Juan"
# edad2 = 25

# print(f"Hola, mi nombre es {nombre2} y tengo {edad2} años.")


##################Lectura y escritura de archivos#####################
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Escritura de archivos
archivo = open("martin.txt", "w")
archivo.write("Hola soy Martin")
archivo.close()

#También puedes utilizar la declaración with para manejar la apertura y cierre de archivos de manera automática.
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)