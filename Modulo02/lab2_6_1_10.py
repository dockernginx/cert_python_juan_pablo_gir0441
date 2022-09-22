'''
Nombre: Juan Pablo Palma Apoderado
Fecha: 22/ sep / 2022
Descripción: Ingresaras un valor flotante para realizar operaciones en escaleras
'''

x = float(input("Ingresa el valor para x: "))

# Escribe tu código aquí.
y = 1/( x + 1 / (x + 1 / (x + 1 / x)) )

print("y =", y)
# 1 ,y = 0.6000000000000001