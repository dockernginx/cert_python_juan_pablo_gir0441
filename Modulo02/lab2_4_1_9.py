'''
Nombre: Juan Pablo Palma Apoderado
Fecha: 22 / sep / 2022
Descripción: Mostrar las millas en kilometros y kilometros en millas 
'''
kilometers = 12.25
miles = 7.38
miles_to_kilometros = miles * 1.61 / 1
kilometros_to_miles= kilometers * 1 / 1.61
print(miles, "Millas son" ,round(miles_to_kilometros, 2), "Kilometros")
print(kilometers, "Kilometros son" , round( kilometros_to_miles, 2), "Millas")