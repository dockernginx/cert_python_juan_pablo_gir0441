'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  6 / oct /2022
Descripción: Esto es un programa que nos da una lista con datos pero lo que tenemos que hacer es 
mostrar la lista pero sin numeros repetidos. 
'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escribe tu código aquí.
#
new_list = my_list
new_list[3:9]
for elem in my_list: 
    if elem in my_list: 
        del my_list[elem]

print("La lista con elementos únicos:")
print(my_list)
