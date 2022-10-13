'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  6 / oct /2022
Descripción: Esto es un programa para convertir l/100km a mpg (milas por galón), y viceversa.Hay que tener 
en cuenta las calculos correctos. 
'''
def liters_100km_to_miles_gallon(liters):
#
# Esta función es para obtener millas
#
 miles = 100 * 1000 / 1609.344 #Lo multiplicamos por mil y dividimos  por 1 milla = 1609.344
 gallon = liters / 3.785411784 #Para obtener los galones dividimos los valores de lioters
 return miles / gallon #Retornamos el valor de la división
def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784  #tomamos como liters que sea igual a 1 galón = 3.7855411784
    kil = miles * 1609.344 / 1000 #lo multipicamos y lo siguiente lo divimos 
    km100 = kil / 100 
    return liters / km100
#
# Escribe tu código aquí.
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
