
'''
Nombre: Juan Pablo Palma Apoderado
Fecha:  6 / oct /2022
Descripción: Esto es un programa que tenemos que usar el metodo .append para introducir los nombres 
a una lista déspues agregar a los integrantes faltantes , borrar a los integrantes faltantes que 
acabamos de introducir y por ultimo ingresar el ultimo integrante y pasarlo al primero de la lista. 
'''
# paso 1
Beatles = []
print("Paso 1:", Beatles)
# paso 2
print("Paso 2:", Beatles)
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
# paso 3
nombre = ''
for miembros in range(2): 
    nombre = input("Agrega el nombre falatante: ")
    Beatles.append(nombre)
print("Paso 3:", Beatles)
# paso 4
del Beatles[3:5]
print("Paso 4:", Beatles)
# paso 5
Beatles.insert(0,"Ringo Starr")
print("Paso 5:", Beatles)

# probando la longitud de la lista
print("Los Fav", len(Beatles))