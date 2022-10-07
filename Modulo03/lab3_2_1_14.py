'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  26 / sep /2022
Descripción: Esto es un programa calcular la altura de una piramide hecha con un numero n de bloques. 
'''
blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	
height=0
while blocks > height: 
    height = height + 1
    blocks = blocks - height

print("La altura de la pirámide:", height)
