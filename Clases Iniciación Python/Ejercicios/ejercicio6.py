"""
Ejercicio 6
Contenidos 7

Arrays:

Crear 4 variables: tipo string, tipo int, tipo float y tipo booleano.

Una vez creadas, añadirlas a un array y mostrar todos los elementos por pantalla
"""

s = "hola"
i = 4
f = 4.54
b = True

caja = [s, i, f, b]

print("Una forma de mostrar elementos de un array")
for i in caja:
    print(i)

print("\n            \n")
print("Otra forma de mostrar elementos de un array\n\n")
for i in range(len(caja)):
    print(caja[i])
