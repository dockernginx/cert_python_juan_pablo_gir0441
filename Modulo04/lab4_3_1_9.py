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
 while div < num: #Condionamos que div sea menor que num 
     if num % div == 0: #Comparamos que num se divisible entre div
       return False  #si es correcto retornamos un valor booleano falso
     div = div + 1 #realizamos un suma en incremento con la variable div
 return True #si se termina la condición retornamos Verdadero

for i in range(1, 20):#Recorre desde 1 hasta 20 
	if is_prime(i + 1):#llamamos a la función y incremanta a un el valor de i que priviene del for
			print(i + 1, end=" ")#terminamos 
print()
