"""
Introducción arrays

len(array)   Indica el tamaño de un array
"""

coches = ["Ford", "Volvo", "BMW", "Opel"]  # Array de strings

numeros = [1, 2, 3, 4] # Array de Integers

"""
coche1 = "Ford"
coche2 = "Volvo"
coche3 = "BMW"

cochesVariables = [coche1, coche2, coche3]

num1 = 1
num2 = 2
num3 = 3
num4 = 4

numerosVariables = [num1, num2, num3, num4]
"""

# Una forma de mostrar los elementos de un array
for i in coches:  #Mostramos por pantalla todos elementos del array coches
    print(i)

# Otra forma de mostrar los elementos de un array
range(start, stop, step)

for i in range(len(coches)):
    print(coches[i])
"""

print(coches[1]) #Mostramos por pantalla el segundo elemento del array coches

print(numeros[0]) #Mostramos por pantalla el primer elemento del array numeros

print(numeros[-1]) # Mostramos por pantalla el último elemento del array numeros
