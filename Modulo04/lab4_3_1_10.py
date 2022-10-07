'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  6 / oct /2022
Descripción: Esto es un programa para convertir l/100km a mpg (milas por galón), y viceversa.Hay que tener 
en cuenta las calculos correctos. 
'''
def liters_100km_to_miles_gallon(liters):
#
# Escribe tu código aquí.
#
 miles = 100 * 1000 / 1609.344
 gallon = liters / 3.785411784
 return miles / gallon
def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    kil = miles * 1609.344 / 1000
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
