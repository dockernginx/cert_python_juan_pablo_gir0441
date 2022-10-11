'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  26 / sep /2022
Descripción: Esto es un programa para realizar los comandos básicos de python para sabe si el año que 
introdujistes es bisiesto o común. 
'''
year = int(input("Introduce un año: "))
if(year <= 1582): 
    print('No esta dentro del período del calendario Gregoriano')
elif year % 4 !=0: 
    print('Año Común') 
elif year % 100 !=0: 
    print('Año Bisiesto')
elif year % 400 !=0:
    print('Año Común') 
else: 
    print('Año Bisiesto')