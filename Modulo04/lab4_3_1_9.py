'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  6 / oct /2022
Descripción: Esto es un programa  que Un número natural es primo si es mayor que 1 
y no tiene divisores más que 1 y si mismo dentro de una rango de numeros que es del 1 al 20. 
'''
def is_prime(num):
#
# Escribe tu código aquí.
#
 div = 2
 while div < num: 
     if num % div == 0: 
       return False
     div = div + 1
 return True 

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
