# FOR
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

#WHILE
contador = 0

while contador < 5:

    print(contador)
    contador += 1

# EJERCICIO
print("Numeros del 1 al 5 multiplicados por 2 con bucle for")
for num in range(1, 6):
    print(num * 2)

print("\nNumeros del 1 al 5 multiplicaods por 2 con bucle while")
numeros = 0

while numeros <= 5:
    print(numeros * 2)
    numeros += 1

# BREAK
print("BREAK")
contador2 = 0

while True:

    print(contador2)
    contador2 += 1

    if contador2 == 5:
        break

# CONTINUE
print("CONTINUE")

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

# PASS
print("PASS")

for i in range(5):
    pass
